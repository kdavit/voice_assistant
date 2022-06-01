import pyjokes
import pyttsx3
import re

language ='en'
category ='neutral'
# comands =["say joke","tell me joke","tell us joke","make joke","make us happy"]
# language =["en","de","es","it","gl","eu"]
# category =['neutral', 'chuck', 'all']

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
    return swicher[argument]

def telljock (text,speak):
    #change category if it is in text
    searchCategory =re.search(".*category.*(neutral|chuck|all)", text)
    if searchCategory:
        category =searchCategory.group(1)
    else:
        category ="neutral"

    #change language if it is in text
    changeLanguage = re.search("(language|in).*(english|german|spanish|italian|galician|basque)", text)
    if changeLanguage:
        language =ChangeL(changeLanguage.group(2))
    else:
        language ="en"
    joke = pyjokes.get_joke(language=language, category=category)
    print("Text you sad : " + text)

    speak(joke)
