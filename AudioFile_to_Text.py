import speech_recognition as sr
#filename="F:\\Dilz\\Future Tools\\zabbix2_1.wav"
filename="C:\\Users\\KDiliz\\Music\\Log_Mon_Error_Code.wav"
r=sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio_data=r.record(source)
    text=r.recognize_google(audio_data)
    print(text)