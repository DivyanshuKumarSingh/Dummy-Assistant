#importing modules

import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random
from speech_recognition import Recognizer,Microphone
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import pywhatkit as pwt
import datetime
from playsound import playsound
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):

    engine.say(audio)
    engine.runAndWait()

def wishme():

    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you ?") 
 
def takeCommand(defau='en-in'):

    #It takes microphone input from the user and returns string output
    r = Recognizer()
    with Microphone() as source:

        print("Listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)
    try:

        print("Recognizing...") 
        query = r.recognize_google(audio,language=defau)
        print(f"User said: {query}\n")

    except Exception as e:

        print("Say that again please...")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dks7050509177@gmail.com', '9352238571')
    server.sendmail('dks7050509177@gmail.com', to, content)
    server.close()    

if __name__=="__main__":

    wishme()


while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:

            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(f'{query}', sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:

            webbrowser.open("youtube.com")

        # elif 'open google' in query:

        #     webbrowser.open("google.com")

        elif 'open stack overflow' in query:

            webbrowser.open("stackoverflow.com")   


        elif 'music' in query:

            music_dir = 'C:\\Users\\ASUS\\Downloads\\mysongs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            

        elif 'the time' in query:

            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif "who made you" in query:

            speak("Prithidev and Divyanshu made me using Python language")

        elif "are you smarter than a human" in query:

            speak("Certainly not but i am trying to improve myself daily")

        elif "tell me a joke" in query:

            foo=["I threw a boomerang one year ago , I now live in constant fear",
            "You don't need a parachute to go for skydiving , you need parachute to go for skydiving twice",
            "Women only call me ugly untill they find out how much money i make. Now they call me ugly and poor !",
            "you are not completely useles , you can always serve for a bad example",
            "Why do cows wear bells , because their horns don't work"]

            speak(random.choice(foo))
        
        elif "are you a male or a female" in query:

            speak("I do not have a gender , i am a robot")

        elif "temperature" in query:

            search="temperature in punjab"
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text

            speak(f"current {search} is {temp}")

        
        elif "google search" in query:

            import wikipedia as googleScrap
            query=query.replace("jarvis","")
            query=query.replace("google search","")
            query=query.replace("google","")
            speak("This is what i found on the web!")

            pwt.search(query)

            try:

                result=googleScrap.summary(query,3)
                speak(result)

            except:

                speak("No data available")

        elif "whatsapp" in query:
            
        
          pwt.sendwhatmsg_instantly("+919352238571","Hi Prithidev , this message is sent to you via jarvis from Prithidev , hope you liked it . This is a completely automated message sent by a robot",17,3)



        elif 'vs code' in query:

            os.startfile('C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')

        elif "word" in query:

            speak("Opening Microsoft Word")
            os.startfile('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE')

        elif "powerpoint" in query:
    
            speak("Opening Microsoft Power Point")
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft PowerPoint 2010.lnk')

        elif "google chrome" in query:
        
            speak("Opening Google Chrome")
            os.startfile('C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk')

        elif "excel" in query:
            
            speak("Opening Microsoft excel")
            os.startfile('"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"')

        # elif "you can take rest now":
        #     speak("ok bye sir , i am always at your service")
        #     exit(0)

        elif "alarm" in query:

            speak("enter the time !")
            time=input(":Enter the time:")

            while True:
                Time_Ac= datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")

                if now==time:
                    speak("Time to wake up Sir !")
                    playsound('C:\\Users\\prithidev ghosh\\Downloads\\ringtone\\ringtone.mp3')
                    speak('Alarm closed')

                elif now>time:

                    break

        elif "please remember" in query:
            rememberMsg=query.replace("remember that","")
            rememberMsg=rememberMsg.replace("jarvis","")
            speak("You tell me to remind you that :"+rememberMsg)
            remember=open('data.txt','w')
            remember.write(rememberMsg)
            remember.close()

        elif "what do you remember" in query:
            remember=open('data.txt','r')
            speak("you told me that"+ remember.read())        
        

        elif 'email' in query:
#          this function will send an email
            try:

                speak("What should I say?")
                content = takeCommand()
                to = "prithidevghosh@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:

                print(e)
                speak("sorry , this email can't be sent")
