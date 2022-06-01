import pyjokes
import pyttsx3
import re
import speech_recognition as sr

r = sr.Recognizer()

language ='en'
category ='neutral'
# comands =["say joke","tell me joke","tell us joke","make joke","make us happy"]
# language =["en","de","es","it","gl","eu"]
# category =['neutral', 'chuck', 'all']

# pyttsx3 used to talk text
def SpeacText(commnad):
    engine = pyttsx3.init()
    engine.say(commnad)
    engine.runAndWait()

# change language
def ChangeL(argument):
     swicher ={
         "english": "en",
         "german":  "de",
         "spanish": "es",
         "italian": "it",
         "italian": "it",
         "galician": "gl",
         "basque": "eu"
     }
     return swicher.get(argument,"en")
def telljock (text):
    comand = re.search("(say|tell|make|play)(\s\w+\s|\s|\s\w+\s\w+\s)(joke||job)", text)
    # change joke category
    searchCategory =re.search(".*category.*(neutral|chuck|all)", text)
    if searchCategory:
        category =searchCategory.group(1)
    else:
        category ="neutral"

    #change language
    changeLanguage = re.search("(change language|in).*(english|german|spanish|italian|galician|basque)", text)
    if changeLanguage:
        language =ChangeL(changeLanguage.group(2))
    else:
        language ="en"
    joke = pyjokes.get_joke(language=language, category=category)
    print("Text you sad : " + text)
    if comand:
        SpeacText(joke)
    else:
        SpeacText("Try again")
        print("Text you sad : " + text)
