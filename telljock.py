import speech_recognition as sr
import pyttsx3
import pyjokes
import re

def telljock(text):
    # r = sr.Recognizer()
    probableComands =["say joke","tell a joke","tell joke","tell me joke","tell us joke","make joke","make us happy","said jest","a joke","make me happy","happy us",
                      "witticisms","make me pleasantry","say something silly", "fool us"," fool around"]

    def checkComand(comand):
        chek = False
        for probable in probableComands:
            if comand in probable:
                chek = True
                break
            else:
                chek =False
        return chek
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
             "galician": "gl",
             "basque": "eu"
         }
         return swicher.get(argument,"en")

    # SpeacText("hello gais")

    # where sounds is listened end SpeacTect use to talk joke
    # with sr.Microphone() as source2:
    #     print("Silence please, calibratin bagrounde noise")
    #     r.adjust_for_ambient_noise(source2,duration=3)
    #     print("calibrated, now speack ...")

        # audio2 = r.listen(source2)
        #
        # Mytext =r.recognize_google(audio2)
        # Mytext =Mytext.lower()

    ifcontains = checkComand(text)
    #comand = re.search("(say|tell|make|play)(\s\w+\s|\s|\s\w+\s\w+\s)(joke)",Mytext)

    # change joke category
    searchCategory =re.search(".*category.*(neutral|chuck|all)",text)
    if searchCategory:
        category =searchCategory.group(1)
    else:
        category ="neutral"

    #change language
    changeLanguage = re.search("change language.*(english|german|spanish|italian|galician|basque)",text)
    if changeLanguage:
        language =ChangeL(changeLanguage.group(1))
    else:
        language ="en"

    joke = pyjokes.get_joke(language=language, category=category)
    print("Text you sad : " + text)
    if ifcontains:
        # SpeacText(pyjokes.get_joke(language="en", category="chuck"))
        SpeacText(joke)
        # print(searchCategory.group(1))
    else:
        SpeacText("Try again")
        print("Text you sad : " + text)