import PyPDF2

class ConvertPDF:

    def convertPDF(self, file):

        # The pdfReader variable is a readable object that will be parsed

        pdfReader = PyPDF2.PdfFileReader(file)
        # discerning the number of pages will allow us to parse through all #the pages
        num_pages = pdfReader.numPages
        count = 0
        text = ""
        # The while loop will read each page
        while count < num_pages:
            pageObj = pdfReader.getPage(count)
            count += 1
            text += pageObj.extractText()

        return text

# if __name__ == "__main__":
#     fileObject = open("051200.pdf", 'rb')
#     pdf = ConvertPDF()
#     text = pdf.convertPDF(fileObject)
#     print(text)