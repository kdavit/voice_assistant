import os
import webbrowser

import nltk
import pyttsx3
import speech_recognition as sr
import wikipedia
from termcolor import colored

from listenAndSpeak import speak
from listenAndSpeak import get_audio


# let's define a function that will convert a list into a string
def listToString(list_n2):
    str1 = " "
    return (str1.join(list_n2))


def wikiSearch(text):
    try:
        # punkt is the function used to devide the string output from the wikipedia page called 'summary' into sentences, thus creating a list.
        nltk.download('punkt')

        search = wikipedia.search(text)
        summary = wikipedia.summary(text)

        # let's count how many sentences there are in the summary
        substring = '.'
        amount_of_sentences = summary.count(substring)

        # bigtext = """how many sentences would you like to be read out of the wikipedia page summary? there are""" + str(
        #     amount_of_sentences)
        # # let's see how many sentences should be read
        # speak(bigtext)
        # amount_of_sentences_read = get_audio()

        if len(summary) >= 1:
            list_n1 = nltk.tokenize.sent_tokenize(summary)  # nltk წინადადებებად ყოფს ტექსტს
            list_n2 = list_n1[:int(4)]

            print(colored("sentences read -->", 'yellow'), summary)
            summary = listToString(list_n2)
            speak(str(summary))

        else:
            for url in search(text, stop=1):
                print(url)

            webbrowser.open(url)
    except:
        speak("try again")

# wikiSearch("Leonardo da Vinci")