import glob
import os
import re
path = r"C:\Users\User\Desktop\zukasi"

text_files = glob.glob(path + "/**/*.pdf", recursive=True)

for filepath in text_files:
    filepath = os.path.splitext(filepath)[0]
    print(os.path.basename(filepath))



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

def checkStartRead(start_page , speak , get_audio):
    speak("do I start read " + str(start_page))

    start_order = get_audio()
    start_reg = r"yes|start|begin|read|play a game"
    match_star_reg = re.search(start_reg, start_order)
    if match_star_reg:
        return True
    else:
        return False
