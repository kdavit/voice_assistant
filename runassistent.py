from listenAndSpeak import get_audio
from intentReader import intentReader
def runAssistent():
    text = get_audio()
    if "anna" in text:
        text = text.replace("anna", "").strip()
        text = text.strip()
        intentD = intentReader()
        for intent in intentD:
            for keyword in intentD[intent]:
                if keyword in text:
                    return intent, text.replace(keyword, "").strip()
    return "No", ""
