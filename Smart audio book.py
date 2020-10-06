import pyttsx3
import PyPDF2
book = open('qp.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
friend = pyttsx3.init()
page = pdfReader.getPage(11)
text = page.extractText()
friend.say(text)
friend.runAndWait()
