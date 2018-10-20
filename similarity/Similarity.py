import string
from scipy.spatial import distance
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Similarity:

    text1tokens = []
    text2tokens = []
    translator = str.maketrans('', '', string.punctuation)

    def stripAndCaseWord(self, word):
        word = word.lower()
        word = word.translate(self.translator)
        return word

    def augmentWithUniqueWords(self, dict1, dict2):
        for key in dict1:
            if key not in dict2:
                dict2[key] = 0

        return dict2

    def cosineSimilarity(self):
        text1count = {}
        text2count = {}


        # Get a count of words in each text
        for word in self.text1tokens:
            word = self.stripAndCaseWord(word)
            if word in text1count:
                text1count[word] = text1count[word] + 1
            else:
                text1count[word] = 1

        for word in self.text2tokens:
            word = self.stripAndCaseWord(word)
            if word in text2count:
                text2count[word] = text2count[word] + 1
            else:
                text2count[word] = 1

        # Build matrix with identical words
        text2count = self.augmentWithUniqueWords(text1count, text2count)
        text1count = self.augmentWithUniqueWords(text2count, text1count)

        # Build lists of word counts w/o words
        vector1 = []
        vector2 = []

        for key in sorted(text1count):
            vector1.insert(-1, text1count[key])
            vector2.insert(-1, text2count[key])

        difference = 1 - distance.cosine(vector1, vector2)

        return difference

    def similarity(self, text1, text2):

        self.text1tokens = word_tokenize(text1)
        self.text2tokens = word_tokenize(text2)
        stopWords = set(stopwords.words('english'))
        self.text1tokens = [w for w in self.text1tokens if not w in stopWords]
        self.text2tokens = [w for w in self.text2tokens if not w in stopWords]
        return self.cosineSimilarity()


# if __name__ == "__main__":
#     text1 = "This is some sample text with, tsome . goofy puncti!"
#     text2 = "This is some other sample text..."
#
#     sim = Similarity()
#     sim.similarity(text1, text2)
#
