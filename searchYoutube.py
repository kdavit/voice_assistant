import urllib.request
import re
import webbrowser


def searchYoutube(text):
    search_keyword = text
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    print()

    get_url = webbrowser.open("https://www.youtube.com/watch?v=" + video_ids[0])
    print("here it is")
