import subprocess
import datetime

def note(text):
    NOTE_STRS = ["make a note","write this down","remeber this"]

    date = datetime.datetime.now()
    file_name = str(date).replace(":","-") +"-note.txt"
    with open(file_name,"w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe",file_name])
    print (file_name)