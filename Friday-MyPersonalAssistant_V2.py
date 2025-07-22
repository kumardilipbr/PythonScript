from typing import Union

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import googlesearch
import psutil
import shutil
import requests,urllib.request,time
from bs4 import BeautifulSoup as bs4
from PyDictionary import PyDictionary
import pyjokes
import subprocess


#from Tools.scripts import google
from googlesearch import search
from psutil._common import sswap
from selenium import webdriver
from selenium.webdriver.chrome import service

#ChromePath = '"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s'



from selenium.webdriver.common.keys import Keys

#engine = pyttsx3.init('sapi5')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#engine.setProperty('voice',"Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
# print(voices[1].id)
#engine.setProperty('voice',voices)
#engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning Dilz")
    elif hour >= 12 and hour < 18:
        speak("Good after noon Dilz")
    else:
        speak("Good Evening Dilz")


    speak("I am Friday, Your Personal BOT")
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"the Current time is {strTime}")

def takeCommand():
    # takes my command from microphone and gives text
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening to you ...")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Trying to recognize ...")
        query = r.recognize_google(audio, language='en-in')
        print("You said : ", query)
    except Exception as e:
        print(e)
        speak("Sorry Dilz, can you please repeat that?")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        speak("How can i help you today?")
        query = takeCommand().lower()
        if 'wikipedia' in query:
            r = sr.Recognizer()
            url='https://www.wikipedia.org'
            with sr.Microphone() as source:
                speak("searching in wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to wikipedia")
                print(results)
                speak(results)

                try:
                    get = r.recognize_google(audio)
                    print(get)
                    webbrowser.get().open_new(url + get)
                except sr.UnknownValueError:
                    print('could not understand')
                except sr.RequestError as e:
                    print('failed to get results'.format(e))


        elif 'play video' in query:
            r = sr.Recognizer()
            webdriver_service = service.Service(
                'C:\\Users\\KDiliz\\Downloads\\operadriver_win64\\operadriver_win64\\operadriver.exe')
            webdriver_service.start()
            driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)
            url = 'https://www.youtube.com/results?search_query='
            with sr.Microphone() as source:
                print('searching for the video')
                speak("searching for the video in Youtube now")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)

                try:
                    get = r.recognize_google(audio)
                    print(get)
                    webbrowser.get().open_new(url + get)
                except sr.UnknownValueError:
                    print('could not understand')
                except sr.RequestError as e:
                    print('failed to get results'.format(e))

        #elif 'Fuck' or 'Fuckoff' or 'Idiot' or 'horrible' or 'damn' or 'dumbo' or 'ass' or 'bloody' or 'jackass' or 'terrific' or not 'super' or not 'awesome' or not 'good' in query:
        #    speak("You are abusive. STOP it.")

        elif 'okok' in query:
            speak("searching in google")
            query = query.replace("google", "")
            speak("According to google")
            for j in search(query, tld="co.in", num=10, stop=5, pause=5):
                print(j)
                webbrowser.get(ChromePath).open_new(j)
                speak("Opened the latest Searches in google")

        elif 'gmail' in query:
            webbrowser.get(ChromePath).open_new('http://gmail.com/')
            speak("gmail is opened")
        #elif 'Awesome' or 'Super' or 'superb' or 'good' in query:
        #    speak("Thanks for the Complements")

        elif 'drive' in query:
            webbrowser.get(ChromePath).open_new('https://drive.google.com/')
            speak("Google Drive is opened")


        elif 'open onenote' in query:
            def open_onenote():
                try:
                    onenote_path = r'C:\Program Files (x86)\Microsoft Office\root\Office16\ONENOTE.EXE'
                    subprocess.Popen(f'start "" "{onenote_path}"', shell=True)
                    print("Opening OneNote")
                except Exception as e:
                    print(f"Error opening OneNote: {e}")
            open_onenote()

        elif 'close one note' in query:
            def terminate_process(process_name):
                try:
                    for process in psutil.process_iter(['pid', 'name']):
                        if process.info['name'] == process_name:
                            pid = process.info['pid']
                            psutil.Process(pid).terminate()
                            print(f"Terminated process {process_name} with PID {pid}")
                            return True

                    print(f"No process named {process_name} found.")
                    return False

                except Exception as e:
                    print(f"Error terminating process {process_name}: {e}")
                    return False
            process_name_to_terminate = 'ONENOTE.EXE'
            terminate_process(process_name_to_terminate)

        elif 'open notepad++' in query:
            def open_notepad():
                try:
                    notepad_path = r'C:\Program Files (x86)\Notepad++\notepad++.exe'
                    subprocess.Popen(f'start "" "{notepad_path}"', shell=True)
                    print("Opening Notepad++")
                except Exception as e:
                    print(f"Error opening Notepad++: {e}")
            open_notepad()

        elif 'close one note' in query:
            def terminate_process(process_name):
                try:
                    for process in psutil.process_iter(['pid', 'name']):
                        if process.info['name'] == process_name:
                            pid = process.info['pid']
                            psutil.Process(pid).terminate()
                            print(f"Terminated process {process_name} with PID {pid}")
                            return True

                    print(f"No process named {process_name} found.")
                    return False

                except Exception as e:
                    print(f"Error terminating process {process_name}: {e}")
                    return False
            process_name_to_terminate = 'notepad++.exe'
            terminate_process(process_name_to_terminate)


        elif 'photos' in query:
            webbrowser.get(ChromePath).open_new('https://photos.google.com/')
            speak("Google Photos is opened")

        elif 'calendar' in query:
            webbrowser.get(ChromePath).open_new('https://calendar.google.com/')
            speak("Google Calendar is opened")

        elif 'leaves' in query:
            my_url = 'https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table'
            webbrowser.get(ChromePath).open_new(my_url)
            response = requests.get(my_url)
            soup = bs4(response.text, "html.parser")
            s = soup.findAll('td')[5].text
            speak(f"You have {s} power")        # Using Selenium we can get the data without opening the web page. Try it for more efficiency of code

        elif 'camera' in query:
            os.system('start microsoft.windows.camera:')

        elif 'automation 1' in query:
            speak("Opening welcome bot")
            os.system("start C:\\Users\\KDiliz\\Videos\\Debut\\welcome.atmx")


        elif 'facebook' in query:
            webbrowser.get(ChromePath).open_new('http://facebook.com/')
            speak("Facebook is opened")
        elif 'whatsapp' in query:
            webbrowser.get(ChromePath).open_new('http://web.whatsapp.com/')
            speak("Whatsapp is opened")
        elif 'say' in query:
            speak("You just said")
            speak(query)

        elif 'play music' in query:
            music_dir = 'C:\\Users\\KDiliz\\Music'
            #songs = os.listdir(music_dir)
            #print(songs)
            #os.startfile(os.path.join(music_dir, songs[0]))
            #speak("music is being played")
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
        #elif 'weather' in query:
        #    webbrowser.get(ChromePath).open("https://www.accuweather.com/en/in/bengaluru/204108/weather-forecast/204108",new=1)
        #    speak("Today's Weather in Bangalore is")

        elif 'meaning' in query:
            dictionary = PyDictionary()
            query1 = query.replace("meaning of", "")
            results = dictionary.meaning(query1)
            speak("The meaning of the word is")
            print(results)
            speak(results)

        elif 'jokes' in query:
           # jokes = pyjokes()
            myjoke = pyjokes.get_joke()
            print(myjoke)
            speak(myjoke)

        elif 'tell me a joke' in query:
           # jokes = pyjokes()
            myjoke = pyjokes.get_joke()
            print(myjoke)
            speak(myjoke)


        elif 'wake up' in query:
            speak("I am awake now !!!")
        elif "computer statistics" in query:
            VMem = psutil.virtual_memory()
            print("Virtual Memory is ", VMem[2])
            speak(f"Virtual Memory is {VMem[2]}")
            SMem: Union[sswap, sswap, sswap, sswap] = psutil.swap_memory()
            print("Swap Memory is ", SMem[3])
            speak(f"Swap Memory is {SMem[3]}")
            CPUPerc = psutil.cpu_percent()
            print("CPU Percentage is ", CPUPerc)
            speak(f"CPU Percentage is {CPUPerc}")
            BootTime = psutil.boot_time()
            BootT = datetime.datetime.fromtimestamp(BootTime).strftime('%c')
            print("Boot Time is ", BootT)
            speak(f"Previous Boot Time was on {BootT}")
            total, used, free = shutil.disk_usage("/")
            print("Total: %d GB" % (total // (2 ** 30)) + " in C Drive")
            print("Free: %d GB" % (free // (2 ** 30)) + " in C Drive")
            #strTime = datetime.datetime.now().strftime("%H:%M:%S")
            #speak(f"The Current time is {strTime}")
            speak(f"Total: %d GB" % (total // (2**30)) + " in C Drive")
            speak(f"Free: %d GB" % (free // (2**30))  + " in C Drive")

        elif 'google' in query:
            r = sr.Recognizer()
            url = 'http://google.com/search#q='
            with sr.Microphone() as source:
                print('search for something on Google')
                speak("search for something on Google")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)

                try:
                    get = r.recognize_google(audio)
                    print(get)
                    webbrowser.get().open_new(url + get)
                except sr.UnknownValueError:
                    print('could not understand')
                except sr.RequestError as e:
                    print('failed to get results'.format(e))
        elif 'weather' in query:
            r = sr.Recognizer()
            url = 'https://www.accuweather.com/en/search-locations?query='
            with sr.Microphone() as source:
                print('Which Place do you want to know the weather of')
                speak("Which Place do you want to know the weather of")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source)

                try:
                    get = r.recognize_google(audio)
                    print(get)
                    webbrowser.get().open_new(url + get)
                except sr.UnknownValueError:
                    print('could not understand')
                except sr.RequestError as e:
                    print('failed to get results'.format(e))

        elif 'sleep' in query:
            speak("I am happy to help you. See you soon again Dilz. Have a great time.")
            exit()
        #else:
        #    webbrowser.open(query)