import speech_recognition as sr
import webbrowser as wb
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


r1 = sr.Recognizer()
r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
    #print('[search edureka: search youtube]')
    print('speak now')
    audio = r1.listen(source)

if 'edureka' in r2.recognize_google(audio):
    r2 = sr.Recognizer()
    url='https://www.edureka.co/search/'
    with sr.Microphone() as source:
        print('search your query')
        audio = r2.listen(source)

        try:
            get = r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))

if 'video' in r1.recognize_google(audio):
    r1 = sr.Recognizer()
    url = 'https://www.youtube.com/results?search_query='
    #url = 'https://www.youtube.com/search/search_query='
    with sr.Microphone() as source:
        print('search for a video')
        audio = r1.listen(source)

        try:
            get = r1.recognize_google(audio)
            print(get)
            #wb.get().open_new(url+get)
            driver=webdriver.Chrome(executable_path="C:\\Users\\KDiliz\\Downloads\\chromedriver.exe")   #spotify_run.py
            driver.get(url+get)     #spotify_run.py
            driver.find_element_by_xpath("//*[@id='video-title']/yt-formatted-string").click()  #spotify_run.py
            driver.fullscreen_window()
            time.sleep(50)
            skip = driver.find_element_by_class_name('ytp-ad-skip-button-container')
            skip.click()

            '''#time.sleep(5)
            # print('now entering while loop')
            while True:
                try:
                    skip = driver.find_element_by_class_name('ytp-ad-skip-button-container')
                    skip.click()
                    time.sleep(25)
                    driver.quit()
                    break
                except:
                    continue'''

            #"//*[@id='skip-button:6']/span/button")))
            #//*[@id="ad-text:y"]
#            element.click()
            #//*[@id="ad-text:13"]
#            time.sleep(300)
            driver.quit() # Closed all the related browsers

        except sr.UnknownValueError:
            print('could not understand')
        except sr.RequestError as e:
            print('failed to get results'.format(e))

'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:\\Users\\KDiliz\\Downloads\\chromedriver.exe")
#driver.get("http://newtours.demout.com/")
##driver.get("http://demo.automationtesting.in/Windows.html")
driver.get("https://www.youtube.com/results?search_query=anantnag+hits")
print(driver.title) # Gives Title of the page
print(driver.current_url)
###driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()
driver.find_element_by_xpath("//*[@id='video-title']/yt-formatted-string").click()
time.sleep(25)
'''
#driver.close() # Closes the Original Browser Only
#driver.quit() # Closed all the related browsers




















