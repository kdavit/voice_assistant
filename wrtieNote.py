import datetime
import subprocess
from listenAndSpeak import *


def note(text):
    speak("What you like me to write down ?")
    text = get_audio()
    date = datetime.datetime.now()
    file_location = "notes/"
    file_name = str(date).replace(":", "-") + "-note.txt"
    file_location += file_name
    with open(file_location, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_location])
    # speak("I've made a note of that.")
    return "Your note successfully created"
