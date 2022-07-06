import urllib.request
import re
import webbrowser


def searchYoutube(text):
    search_keyword = text.replace(" ","+")
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print('aqa var')

    webbrowser.open("https://www.youtube.com/watch?v=" + video_ids[0])

    return "here it is"
