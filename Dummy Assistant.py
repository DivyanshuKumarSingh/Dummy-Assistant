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
    
#     this function greets with good morning/good afternoon/good evening according to the current local time

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
    
#     main function to exexute the whole program

    wishme()


while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            
#             if user says "wikipedia" , then this function will be trigerred and it will search for the asked query on wikipedia.com

            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(f'{query}', sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            
#             if user says "open youtube" this function will be trigerred and youtube.com will be opened in user's default browser

            webbrowser.open("youtube.com")

        elif 'open stack overflow' in query:
            
#             if user says "open stack overflow" , this function will be trigerred and stackoverflow.com will be opened

            webbrowser.open("stackoverflow.com")   


        elif 'music' in query:
            
#             if user says "music" , this function will be trigerred and a music will be played from local playlist

            music_dir = 'C:\\Users\\ASUS\\Downloads\\mysongs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            

        elif 'the time' in query:
            
#             if user says "the time" , this function will be trigerred and will say the current local time

            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif "who made you" in query:
            
 #             if user says "who made you" , this function will be trigerred and will say the names of the developers of this program

            speak("Prithidev and Divyanshu made me using Python language")

        elif "are you smarter than a human" in query:
            
 #             if user says "are you smarter than a human" , this function will be trigerred and will answer in an intelligent manner

            speak("Certainly not but i am trying to improve myself daily")

        elif "tell me a joke" in query:
            
 #             if user says "tell me a joke" , this function will be trigerred and will say a random joke , randomly picked from the list "foo"

            foo=["I threw a boomerang one year ago , I now live in constant fear",
            "You don't need a parachute to go for skydiving , you need parachute to go for skydiving twice",
            "Women only call me ugly untill they find out how much money i make. Now they call me ugly and poor !",
            "you are not completely useles , you can always serve for a bad example",
            "Why do cows wear bells , because their horns don't work"]

            speak(random.choice(foo))
        
        elif "are you a male or a female" in query:
            
 #             if user says "are you male or a female" , this function will be trigerred and will answer in an intelligent manner          

            speak("I do not have a gender , i am a robot")

        elif "temperature" in query:
            
#             if user says "temperature" , this function will be trigerred and will say the current temperature          


            search="temperature in punjab"
            url=f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data=BeautifulSoup(r.text,"html.parser")
            temp=data.find("div",class_="BNeawe").text

            speak(f"current {search} is {temp}")

        
        elif "google search" in query:
            
 #             if user says "google search" , this function will be trigerred and will search for the query on google.com and will dictate the results          


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
           
#             if user says "whatsap" , this function will be trigerred and will send a message on whatsapp          
 
        
          pwt.sendwhatmsg_instantly("+919352238571","Hi Prithidev , this message is sent to you via jarvis from Prithidev , hope you liked it . This is a completely automated message sent by a robot",17,3)



        elif 'vs code' in query:
            
#             if user says "vs code" , this function will be trigerred and vs code will be opened       


            os.startfile('C:\\Users\\ASUS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')

        elif "word" in query:
            
 #             if user says "word" , this function will be trigerred and microsoft word will be opened       

            speak("Opening Microsoft Word")
            os.startfile('C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE')

        elif "powerpoint" in query:
    
 #             if user says "powerpoint" , this function will be trigerred and powerpoint will be opened       
            speak("Opening Microsoft Power Point")
            os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft PowerPoint 2010.lnk')

        elif "google chrome" in query:
            
#             if user says "google chrome" , this function will be trigerred and google chrome will be opened       
        
            speak("Opening Google Chrome")
            os.startfile('C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk')

        elif "excel" in query:
            
#             if user says "excel" , this function will be trigerred and excel will be opened       
            
            speak("Opening Microsoft excel")
            os.startfile('"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"')

        elif "alarm" in query:
            
 #             if user says "alarm" , this function will be trigerred and will ask to input the time in which user need an alarm and the alarm will be trigerred on that time       
            
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
            
#             if user says "please remember" , this function will note whatever the user said and will save it in data.txt file      
            
            rememberMsg=query.replace("remember that","")
            rememberMsg=rememberMsg.replace("jarvis","")
            speak("You tell me to remind you that :"+rememberMsg)
            remember=open('data.txt','w')
            remember.write(rememberMsg)
            remember.close()

        elif "what do you remember" in query:
            
#             if user says "what do you remember" , this function will be say whatever is recorded on data.txt file       
            
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
