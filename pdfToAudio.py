# Python script to PDF to Audio
import PyPDF2
import os
import pyttsx3
import re
from listenAndSpeak import speak


def transformPDFtoAudio(text):
    path = r"C:\Users\David\Documents\Neural Network From Scratch by Harrison Kinsley  Daniel Kukieła (z-lib.org).pdf"
    pdf_file = open(path, 'rb')
    read_pdf = PyPDF2.PdfReader(pdf_file, strict=False)

    nuber_of_pages = len(read_pdf.pages)

    for i in range(0, nuber_of_pages):
        page = read_pdf.pages[i]
        page_content = page
        speak(page_content)
