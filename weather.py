import requests
from bs4 import BeautifulSoup
from googletrans import Translator
from listenAndSpeak import speak
import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


def weather(city, date=datetime.date.today()):  # date უნდა იყოს აქ და არა today, ქვემოთ რექვესთში date-ს გადასცემდი რომელსაც ინიციალიზაცია არსად ქონდა
    try:
        text = city.split()
        city = text[0]
        # today = datetime.date.today() ეს ხაზი ზედმეტია

        # dateGuess-დან get_date ფუნქცია უნდა გამოიყენო მთლიანად ტექსტზე, სიტყვიერად ვამბობ თარიღს, ამიტომ პირდაპირ სასურველი ფორმატით თარიღს არ გადმოგცემ
        if len(text) > 1:
            date = text[1]
        city += "+weather"
        res = requests.get(
            f'https://www.google.com/search?q={city}+{date}&oq={city}+{date}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
            headers=headers)
        print("Searching...\n")
        soup = BeautifulSoup(res.text, 'html.parser')
        location = soup.select('#wob_loc')[0].getText().strip()
        time = soup.select('#wob_dts')[0].getText().strip()
        info = soup.select('#wob_dc')[0].getText().strip()
        weather = soup.select('#wob_tm')[0].getText().strip()
        collecttext = "in " + location + " at " + time + " it's " + info + " and temperature is " + weather + "°C"
        translator = Translator()
        translated_text = translator.translate(collecttext)
        print(translated_text.text)  # აჯობებს რომ თან დავბეჭდოთ
        return translated_text.text
    except:
        return "can't find city"


# speak(weather("tbilisi june 29th"))