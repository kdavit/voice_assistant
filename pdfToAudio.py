# Python script to PDF to Audio
import speech_recognition as sr
import pyttsx3
import PyPDF2
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer, LTChar ,LTTextLine, LTText, LTTextBox, LTLine
import glob
import os
import re

def transformPDFtoAudio(speak,get_audio):
    path = r"C:\Users\User\Desktop\zukasi\ASP.NET Core in Action ( PDFDrive ).pdf"
    pdf_file = open(path,'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file, strict=False)

    nuber_of_pages = read_pdf.getNumPages()
    pgNub = "number of pages is ",nuber_of_pages
    speak(pgNub)
    print(nuber_of_pages)

    start_page = setStartPage(speak,get_audio)

    speak("do I start read " + str(start_page))

    start_order = get_audio()
    start_reg = r"yes|start|begin|read|play a game"
    match_star_reg = re.search(start_reg, start_order)

    if match_star_reg == None:
        start_page = setStartPage(speak,get_audio)

    for i in range(int(start_page), nuber_of_pages):
        page = read_pdf.getPage(i)
        page_content = page.extractText()
        speak(page_content)


def setStartPage (speak,get_audio):
    speak("Set the start page ")
    start_page = get_audio()
    regex = r"\d+"
    match_stp = re.findall(regex, start_page)
    if match_stp:
        start_page = match_stp[0]
    else:
        start_page = 0
    return start_page

    # pdfReader = PyPDF2.PdfFileReader(pdfbookAdres)
    # for page_num in range(pdfReader.numPages):
    #     text = pdfReader.getPage(page_num).extractText()  ## extracting text from the PDF
    #     cleaned_text = text.strip().replace('\n', ' ')  ## Removes unnecessary spaces and break lines
    #     print(cleaned_text)
    #     # reading the text
    # speak(cleaned_text)
# https://python.plainenglish.io/how-to-convert-a-pdf-file-to-an-audio-mp3-file-using-python-dbbf21f4d5b4


    # pdfreader = PyPDF2.PdfFileReader(open(pdfbookAdres,'rb'))
    # f = open("pdfText.txt", "r+",encoding='utf-8')
    # listContent =[]
    # for page_layout in extract_pages(pdfbookAdres):
    #     listContent.append(page_layout)
    # i = 0
    # breakpoint = False
    # for element in listContent[4]:
    #     if isinstance(element, LTTextContainer):
    #         print(element)
            # if "Contents" in element.get_text():
            #     print(element.get_text())
            #     printContent(listContent[i])
                # breakpoint = True
                # break
        # i += 1
        # if breakpoint:
        #     break

# def printContent(contentspage):
#     for elemnt in contentspage:
#         if isinstance(elemnt, LTTextContainer):
#             print(elemnt.get_text())
    # creating a PdfFileReader object
