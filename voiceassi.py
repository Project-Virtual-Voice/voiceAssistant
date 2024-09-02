import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
# import requets
import shutil
import google.generativeai as genai
import re
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen


genai.configure(api_key=os.environ["GEMINI_API_KEY"])


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 190)

def preprocess_text(text):
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    return cleaned_text.strip()

def speak(audio):
    original_audio = audio
    cleaned_audio = preprocess_text(audio)
    print("Assistant:", original_audio)

    sentences = audio.split('.')
    for sentence in sentences:
        if sentence.strip():
            engine.say(sentence.strip())
            engine.runAndWait()
            time.sleep(0.1)
           
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if (hour>=4 and hour<12):
        speak("Good Morning")
    elif (hour>=12 and hour<17):
        speak("Good Afternoon")
    elif (hour>=17 and hour<21):
        speak("Good Evening")
    else:
        speak("Hello!")

    combined_text = "I am your voice Assistant, Jarvis."
    speak(combined_text)

    
def username():
    speak("What should i call you?")
    uname = takeCommand()

    if uname == "None":
        speak("I didn't catch that. What should i call you?")
        uname = takeCommand()

    if uname != "None":
        speak("Welcome Mister")
        speak(uname)
    else:
        speak("Unable to recognize your name. Please try again later.")


 
def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for ambient noise
        r.pause_threshold = 1
        r.energy_threshold = 100  # Adjust this value based on your environment
        audio = r.listen(source, timeout=5, phrase_time_limit=5)
  
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language ='en-in')
        print(f"You: {query}\n")
  
    except Exception as e:
        print(e)    
        print("Unable to Recognize your voice.")  
        return "None"
     
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


def get_gemini_response(contents):
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')

        response = model.generate_content(
            contents=contents,
            generation_config=None,
            safety_settings=None,
            stream=False,
            tool_config=None,
            tools=None,
            request_options=None
        
        )

        if hasattr(response, 'text'):
            return response.text.strip()
        else:
            return "No content attribute found in the response"

    except Exception as e:
        print(f"Error interacting with Gemini AI: {e}")
        return "Sorry, I'm having trouble connecting to Gemini AI right now."
    
def activate_assistant():
    speak("How can i assist you?")

    while True:
        command = takeCommand().lower()

        if command in ["exit", "stop", "quit"]:
            speak("Goodbye")
            break

        elif "ask AI" in command or "ask gemini" in command:
            response = get_gemini_response(command)
            # print(response)
            speak(response)

        elif "open youtube" in command:
            speak("Here you go to Youtube")
            webbrowser.open('youtube.com')
            break

        elif "open google" in command:
            speak("Here you go to Google")
            webbrowser.open('google.com')
            break

        elif "open stack overflow" in command:
            speak("Here you go to stackoverflow.happy coding")
            webbrowser.open('stackoverflow.com')
            break
        
        elif "wikipedia" in command:
            speak("Searching wikipedia")
            command=command.replace("wikipedia","")
            results=wikipedia.summary(command,sentences=3)
            speak("According to wikipedia..")
            print(results)
            speak(results)
            break

        elif  "play music" in command or "play song" in command:
            speak("Here you go with your music")
            music_dir=r"C:\MY MUSIC"
            songs=os.listdir(music_dir)
            print(songs)
            random=os.startfile(os.path.join(music_dir,songs[0]))
            # spotify_url="https://open.spotify.com/album/0a183xiCHiC1GQd8ou7WXO?si=koTFQMMuQPWYQbE1ckgx6Q"
            # webbrowser.open('spotify_url')
            break

        elif "time" in command:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir your time is {strTime}")
            break

        elif "open microsoft edge" in command:
            codePath=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            os.startfile(codePath)
            break

        elif "how are you" in command or "how r u" in command :
           speak(f"I am fine,i hope you are doing well")
           speak(f"so ,how are you sir")
           

        elif "fine" in command or "good" in command:
         speak(f"Good to see u fine ")
         break

        elif "change my name to" in command:
         command=command.replace("change my name to","")
         uname=command
         break

        


        else:
            speak("Is there anything else I can help you with?") 

if __name__ == '__main__':
    clear = lambda: os.system('cls')
    
    clear()


    while True:
        speak("Say 'Hey Jarvis' to activate the assistant")
        query = takeCommand().lower()

        if 'hey jarvis' in query:
            wishMe()
            username()
            activate_assistant()
        else:
            continue
