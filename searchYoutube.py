import urllib.request
import re
import webbrowser


def searchYoutube(text):
    try:
        search_keyword = text.replace(" ", "+")
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        webbrowser.open("https://www.youtube.com/watch?v=" + video_ids[0])
    except:
        return "please say search words"

    return "here it is"
