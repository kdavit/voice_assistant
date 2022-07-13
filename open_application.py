from listenAndSpeak import speak
from os import system


def openApplication(text):
    try:
        apps_dict = {
                     "chrome": ["google", "search", "web browser", "chrome", "browser"],
                     "msedge": ["ie", "msedge", "edge"],
                     "Notepad": ["note", "notes", "notepad"],
                     "VLC": ["vlcplayer", "player", "video player"],
                     "excel": ["excel", "msexcel", "sheet", "winexcel"],
                     "powerpoint": ["slide", "powerpoint", "ppt"],
                     "winword": ["word", "msword"]
                     }

        for app in apps_dict:
            if text in apps_dict[app]:
                system("start {0}".format(app))
                return "opening right up"

        system("start {0}".format(text))

        return ""
    except:
        return "Something went wrong."