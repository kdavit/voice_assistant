import webbrowser
import speech_recognition as sr
import wikipedia
import pyttsx3
from googlesearch import search
import nltk 
from termcolor import colored
import os
from nltk import PunktSentenceTokenizer

#let's add some colors.....
os.system('color')

#let's define a function that will convert a list into a string
def listToString(list_n2): 
    str1 = " " 
    return (str1.join(list_n2))

#let's define a function that will be used as an audio input for our search engine
def get_audio():
    recognize = sr.Recognizer()
    with sr.Microphone() as source2:
        
        print("Silence please, calibrating background noise")
        recognize.adjust_for_ambient_noise(source2,duration=3)
        print("Calibrated, now speack ...")

        audio2 = recognize.listen(source2)

        Mytext =recognize.recognize_google(audio2)
        Mytext =Mytext.lower()

        return Mytext

#punkt is the function used to devide the string output from the wikipedia page called 'summary' into sentences, thus creating a list.
nltk.download('punkt')

#let's define the engine we are going to be using for tts(text to speech)
engine = pyttsx3.init()

#let's ask the user the choose the input device
print("""what would you prefer to use as an input device, your microphone or your keyboard? 
type 1 for""", colored('AUDIO INPUT (voice)','green') ,
""" type 2 for""" , colored('MANUAL INPUT (keyboard)','green'))

preference = input("")

if preference == '1' :
    query = get_audio

else :
    query = input("what would you like to search for?\n")


search = wikipedia.search(query)
summary= wikipedia.summary(query)
print("            ")

#let's count how many sentences there are in the summary
substring = '.'
amount_of_sentences = summary.count(substring)

#let's see how many sentences should be read 
print("""how many sentences would you like to be read out of the wikipedia page summary? 
there are""",amount_of_sentences,"""sentences in the summary 
if you want all of them to be read then write""" , colored ('ALL','red'), """, if not write amount of sentences you would like to be read... """)
amount_of_sentences_read = input()
print("     ")

if len(summary) >= 1:
    if amount_of_sentences_read == 'all' or amount_of_sentences_read == 'ALL' or amount_of_sentences_read == 'All': 
        print(summary)
        engine.say(str(summary))
        engine.runAndWait()

    else :
        list_n1 = nltk.tokenize.sent_tokenize(summary) #nltk წინადადებებად ყოფს ტექსტს
        list_n2 = list_n1[:int(amount_of_sentences_read)]
        if amount_of_sentences_read == '1' : 
          print(colored("here is the full summary --> ",'yellow'), summary , colored(".... but only the first sentence will be read as you told me to ..." , 'yellow'))
    
        else:
            print(colored('here is the full summary --> ','yellow'), summary , colored("... but only first",'yellow') , colored(amount_of_sentences_read,'yellow') , colored(' sentences are going to be read, just as you told me to...','yellow'))

    summary = listToString(list_n2)
    engine.say(str(summary))
    engine.runAndWait()
    print("    ")
    print(colored("sentences read -->" , 'yellow') , summary)

else:
    for url in search (query, stop=1) : 
        print(url)

    webbrowser.open(url)   


