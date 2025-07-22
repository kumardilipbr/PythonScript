import time
import pyttsx3 # importing the pyttsx library
engine = pyttsx3.init() # initialisation
import pyaudio
import os

#engine.say("My first code on text-to-speech")
#engine.say("Thank you, Geeksforgeeks")
#engine.say("This is so exciting. I am so very excited, Do you know?")

#pyaudio().
#engine.say("Alexa")
os.system("start C:\\Users\\KDiliz\\Desktop\\Calling_Alexa.m4a")
time.sleep(4)
engine.runAndWait()
os.system("TASKKILL /F /IM vlc.exe")
#time.sleep(2)
#engine.say("What is the time")
#engine.runAndWait()
time.sleep(2)
engine.say("what is the weather today")
engine.runAndWait()
time.sleep(14)
os.system("start C:\\Users\\KDiliz\\Desktop\\Calling_Alexa.m4a")
time.sleep(4)
os.system("TASKKILL /F /IM vlc.exe")
engine.say("what is the time")
engine.runAndWait()
