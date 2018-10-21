import string
import math


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

    def doTheMath(self, vector1, vector2):

        numerator = 0
        denom1, denom2 = (0, 0)
        for i in range(0, len(vector1)):
            numerator += (vector1[i] * vector2[i])
            denom1 += vector1[i]**2
            denom2 += vector2[i]**2

        return numerator / (math.sqrt(denom1) * math.sqrt(denom2))



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

        difference = self.doTheMath(vector1, vector2)

        return difference

    def similarity(self, text1, text2):

        self.text1tokens = text1.split()
        self.text2tokens = text2.split()
        return self.cosineSimilarity()


# if __name__ == "__main__":
#     text1 = "This is some sample text with, tsome . goofy puncti!"
#     text2 = "This is some other sample text..."
#
#     sim = Similarity()
#     sim.similarity(text1, text2)

