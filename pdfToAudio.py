# Python script to PDF to Audio
import PyPDF2
import os
import pyttsx3
import re
from listenAndSpeak import speak
def transformPDFtoAudio(text):
    path = r"C:\Users\User\Desktop\zukasi\ASP.NET Core in Action ( PDFDrive ).pdf"
    pdf_file = open(path,'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)

    nuber_of_pages = read_pdf.getNumPages()

    for i in range(0, nuber_of_pages):
        page = read_pdf.getPage(i)
        page_content = page.extractText()
        speak(page_content)
