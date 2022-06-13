import datetime
import subprocess
from listenAndSpeak import *

def note(text):
    speak("What you like me to write down ?")
    text = get_audio()
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])
    # speak("I've made a note of that.")
    return "Your note successfully created"
