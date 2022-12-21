import pyttsx3#text to speech library (works offline)
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime
from selenium import webdriver#browser automation tool
import time

#to take the command from user 
def command():
    r=sr.Recognizer()#creating an instance of the Recognizer class
    with sr.Microphone() as source:#install PyAudio to work with microphone and default system microphone acts as source for sr
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)#listen method of Recognizer class...Records input from source until silence is detected
        try:#using exception handling in case the speech isnt recognizable
            print("Recognizing...")
            query=r.recognize_google(audio,language='en')#to recognize the audio recorded by listen method
            print(query)
        except Exception as e:
            print(e)
            print("failed to understand Can you say that again?")
            speech("failed to understand Can you say that again")
            return "None"
        return query
    
#text to speech method 
def speech(audio):
    engine=pyttsx3.init()#this function gets a reference to pyttx3.engine instance
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)#to change the voice 0 for male and 1 for female
    engine.say(audio)#to pass the input text to be spoken
    engine.runAndWait()#it processes the command

def date_and_time(day,date,time):
    now=datetime.datetime.now()
    if date == 1:
         speech("Today is {}".format(now.strftime("%d %B")))#strftime formats date object into readable strings
    if day == 1 :
         speech("Today is {}".format(now.strftime("%A")))
    if time == 1:
         speech("It is {}".format(now.strftime("%I:%M %p")))#%I gives hours between 0 to 12 %p means tha time in am,pm format

def hello():
    speech("hello sir I am Friday Your desktop assistant How may i help you")

def search_web(query):
    query=query.replace('search','')
    driver = webdriver.Chrome(executable_path=r'C:/Users/Sarthak/Documents/chromedriver.exe')#depending on browser.Instance of chrome with path to the webdriver
    driver.implicitly_wait(1)#driver will wait for a max 1 sec before throwing an exception
    driver.maximize_window()#chrome will open in full screen mode
    driver.get('http://www.google.com/search?q='+query)
    time.sleep(5)#halts the execution of program for the given time

def Headlines():
     news = webbrowser.open_new_tab("www.timesofindia.com")#opening times of india website in the new tab
     speech("Here are the latest headlines Happy reading ")
     time.sleep(5)

def creator():
    speech("I was created as a Python project by Mehul Nishant Sarthak and Priyanshu")

def features():
    speech("I can do various tasks like tell you the day ,date and time ,opening the browser,search on the web ,latest news,and can also tell about anything from wikipedia")


def query():
    hello()
    while(True):
        query=command().lower()
        if "wikipedia" in query:
            query=query.replace("wikipedia","")
            result="according to wikipedia"+wikipedia.summary(query,sentences=3)#number of sentences we want from wikipedia 
            speech(result)
            time.sleep(10)
        elif "open google" in query:
            webbrowser.open("www.google.com")
        elif "time" in query:
            date_and_time(0,0,1)
        elif "date" in query:
            date_and_time(0,1,0)
        elif "day" in query:
            date_and_time(1,0,0)
        elif "bye" in query:
            speech("closing assistant")
            exit()
        elif "search" in query:
            search_web(query)
        elif 'news' in query:
            Headlines()
        elif 'who created you' in query:
            creator()
        elif 'what can you do' in query or 'what are your features' in query:
            features()

while(1):
    query()
