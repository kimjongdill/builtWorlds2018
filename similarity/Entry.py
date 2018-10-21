import Similarity
import ConvertPdf
import requests
import io
import json

def scoreHandler(event, context):
    file1Url = event["file1"]
    file2Url = event["file2"]

    file1 = requests.get(file1Url)
    file2 = requests.get(file2Url)

    if file1.status_code == 200 and file2.status_code == 200:
        sim = Similarity.Similarity()
        pdf = ConvertPdf.ConvertPDF()
        fileStream1 = io.BytesIO(file1.content)
        fileStream2 = io.BytesIO(file2.content)
        text1 = pdf.convertPDF(fileStream1)
        text2 = pdf.convertPDF(fileStream2)
        returnVal = {}
        returnVal["sim"] = sim.similarity(text1, text2)


        return json.dumps(returnVal)

    return 0

if __name__ == "__main__":
    event = {}
    context = ""
    event["file1"] = "http://www.georgedill.net/bw2018/051200.pdf"
    event["file2"] = "http://www.georgedill.net/bw2018/051200.pdf"
    print(scoreHandler(event, context))
