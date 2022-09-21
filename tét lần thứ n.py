
import mimetypes
import pyttsx3 
from pyttsx3 import *
import speech_recognition as sr
from speech_recognition import *
import datetime
import requests
import wikipedia
from wikipedia import *
import webbrowser as wb
from youtube_search import YoutubeSearch
from datetime import datetime
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
path = ChromeDriverManager().install()
#miệng
AI_mouth = pyttsx3.init()
#tai
AI_ear = sr.Recognizer()
#Não
AI =""
#Đặt Tên Bot Tại Đây
GZI = "GZI : "
yous ="Hoàng"
voices = AI_mouth.getProperty("voices")
AI_mouth.setProperty("voice",voices[0].id)
def ear():
    AI_ear = sr.Recognizer()
    with sr.Microphone() as source:
        audio = AI_ear.listen(source, phrase_time_limit=5)
        try:
            query = AI_ear.recognize_google(audio, language="vi-VN")
            print(query)
        except sr.UnknownValueError:
            speak("I don't understand what you're saying. Please say it again")
    return query

def welcome():
    hour=datetime.now().hour
    if hour < 12:
        speak("good morning " + yous)
    elif hour >= 13 and hour < 19:
        speak("good afternoon " + yous)
    elif hour >= 19 and hour < 24:
        speak("good evening " + yous)
        pass

def current_weather():
    speak(yous+" Where do you want to see the weather?")
    ow_url = "https://api.openweathermap.org/data/2.5/weather?"
    city = ear()
    if not city:
        pass
    api_key = "d2715dcf1ff713e59095eddc07088c23"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        visibility = data["visibility"]
        wind = data["wind"]
        wind_speed = wind["speed"]
        suntime = data["sys"]
        sunrise = datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.now()
        content = """
        Weather in {city}  {day} {month},{year} at {hour} {minute} is
        Temperature {temp} degrees Celsius
        Air pressure {pressure} hetopascal 
        Humidity {humidity}%
        The sun rises in {hourrise} {minrise}
        The sun goes down {hourset} {minset}
        Visibility over {visibility} meters
        Wind speed is about {wind} meters per second
        """.format(city=city, hour=now.hour,minute=now.minute,\
         day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour,\
          minrise = sunrise.minute,hourset = sunset.hour, minset = sunset.minute,\
        wind=wind_speed, visibility=visibility, temp = current_temperature,\
         pressure = current_pressure, humidity = current_humidity)
        speak(content)
    else:
        speak("The address you mentioned was not found.\
            Please reuse or use other functions of "+GZI)
def speak(voices):
    print(GZI + voices)
    AI_mouth.say(voices)
    AI_mouth.runAndWait()
    AI = speak

def tell_me_about():
    try:
        speak("What do you want to hear about?")
        text = ear()
        if "là ai" in text:
            text = text.replace("who is","")
        if "là gì" in text:
            text = text.replace("what is","")
        wikipedia.set_lang("vi")
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0])
        for content in contents[1:]:
            speak(f"Do you want to hear more about {text} ?")
            ans = ear()
            if "yes" not in ans:
                break    
            speak(content)

        speak('Thank you for listening!!!')
        speak("Does "+yous+" ask for anything else?")
    except:
        speak("I can't define your term. \
            Please reuse or use my other function")
        speak("Does "+yous+" ask for anything else?")
def play_song():
    speak("What song do you want to listen to?")
    song =ear()
    while True:
        final = YoutubeSearch(song , max_results=10).to_dict()
        if final:
            break
    song = "https://www.youtube.com/results?search_query=" + song
    wb.get().open(song)
    speak("Your song has been played")
#lỗi lạ đéo biết sửa gút bye mai cót
def open_google_and_search(you):
    search_for = you.split("search", 1)[1]
    speak('Okay!')
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)
    time.sleep(10)

while True:
    with sr.Microphone() as mic:
        speak("i'm listening to you")
        audio = AI_ear.listen(mic)
    print("GZI : ...")
    try:
        you = AI_ear.recognize_google(audio,language="vi")
    except sr.UnknownValueError:
        speak("I do not understand")
        continue
    print(yous + " : " + you)
    if you == "":
        speak("I do not understand")
        continue
    elif "hello" in you or "hi" in you : 
        welcome()
    elif "today" in you :
        Time =datetime.now().strftime(" %m/%d/%Y")
        speak("Today is "+ Time)
    elif "time" in you :
        nTime = datetime.now().strftime(" %H:%M:%S, %m/%d/%Y")
        speak(nTime)
    elif "Visual Studio code" in you :
        app = 'D:\Microsoft VS Code\Code.exe'
        os.startfile(app)  
        speak(you+" request has been completed")
    elif "stop" in you or "rừng"in you :
        speak("Good Bye, see you later "+yous)
        break
    elif "weather" in you:
        current_weather()
    elif "Đạt Vina" in you:
        speak("Là thằng chó đẻ ăn cứt 400 triệu")
    elif "want to find" in you:
        tell_me_about()
    elif "music" in you:
        play_song()
    elif "search" in you or "kiếm" in you:
        open_google_and_search(you)
    elif "kiệt" in you or "Kiệt"in you:
        speak("Kiệt lặc ăn cứt")
        speak("bú đít tao")
        speak("ỉa chảy")
    else:
        speak("tôi khổng hiểu")