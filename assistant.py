import subprocess
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests
import pyjokes
import smtplib
import ctypes
import time
import google.generativeai as genai
import re
from ecapture import ecapture as ec

genai.configure(api_key=os.environ["GEMINI_API_KEY"])


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 180)

assname="Jarvis"

def preprocess_text(text):
    cleaned_text = re.sub(r'[^\w\s.,:!?]', '', text)
    return cleaned_text.strip()

def speak(audio):
    original_audio = audio
    cleaned_audio = preprocess_text(audio)
    print("Assistant:", original_audio)

    sentences = re.split(r'(?<=[.!?]) +', cleaned_audio)
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
    
    
    combined_text = f"I am your voice Assistant, {assname}."
    speak(combined_text)

    
def username():
    speak("What should i call you?")
    uname = takeCommand()

    if uname == "None":
        speak("I didn't catch that. What should i call you?")
        uname = takeCommand()

    if uname != "None":
        speak(f"Welcome, Mister {uname}")
    else:
        speak("Unable to recognize your name. Please try again later.")

input_method = None

def takeCommand():
    global input_method
    
    if input_method is None:
        speak("Choose input method:")
        print("[1] Type your command")
        print("[2] Speak your command")

        choice = input("Enter 1 or 2: ").strip().lower()
    
        if choice == "1":
            input_method = "type"
        elif choice == "2":
            input_method = "voice"
        else:
            print("Invalid choice! Please enter 1 or 2.")
            return takeCommand()
        
    if input_method == "type":
        command = input("Enter your command: ").strip().lower()
        return command
    elif input_method == "voice":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for ambient noise
            r.pause_threshold = 1
            r.energy_threshold = 2000  # Adjust this value based on your environment
            audio = r.listen(source, timeout=10, phrase_time_limit=5)
            
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language ='en-in')
        print(f"You: {query}\n")
        return query.lower()

    except Exception as e:
        print(f"error: {e}")    
        print("Unable to Recognize your voice. Try again or type your command.")  
        return takeCommand()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ayyanjsk@gmail.com', 'tsec kbko wbmk gbpi')
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
    

def handle_follow_up():
    speak("Is there anything else I can help you with?") 
    follow_up = takeCommand().lower()
    if follow_up in ["no", "nothing", "no thanks"]:
        speak("Okay, I'll be here if you need me.")
        return False
    return True


def open_in_chrome(url):
    chrome_path= "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    
def activate_assistant():
    global exit_flag
    speak("How can i assist you?")

    while not exit_flag:
        command = takeCommand().lower()

        if command in ["exit", "stop", "quit"]:
            speak("Goodbye")
            exit_flag = True
            break

        elif "ask ai" in command or "ask gemini" in command:
            response = get_gemini_response(command)
            speak(response)
            

        elif "open youtube" in command:
            speak("Here you go to Youtube")
            open_in_chrome('youtube.com')

            time.sleep(2)
            

        elif "open google" in command:
            speak("Here you go to Google")
            open_in_chrome('google.com')

            time.sleep(2)
            

        elif "open stack overflow" in command:
            speak("Here you go to stackoverflow.happy coding")
            open_in_chrome('stackoverflow.com')

            time.sleep(2)
            
        
        elif "wikipedia" in command:
            speak("Searching wikipedia")
            command=command.replace("wikipedia","")
            results=wikipedia.summary(command,sentences=3)
            speak("According to wikipedia..")
            print(results)
            speak(results)

            time.sleep(2)
            

        elif "search" in command:
            command = command.replace("search", "").strip()
            if command:
                query_url= f"https://www.google.com/search?q={command.replace(' ', '+')}"
                open_in_chrome(query_url)
                time.sleep(2)
            else:
                speak("What would you like to search for?")
        

        elif "news" in command:
            api_key = os.getenv("newsapi")
            url = f'https://gnews.io/api/v4/search?q=technology&lang=en&country=us&max=5&apikey=61ec3218ce70467133506eb2bf1cde59'  

            try:
                response = requests.get(url)
                data = response.json()
                
                articles = data.get("articles", [])    
                if not isinstance (articles, list) or not articles:
                    speak("No news articles found!")
                    return
                        
                else:
                    print('''==================== TIMES OF INDIA ====================''' + '\n')
                    speak("Here are the top news headlines")


                for i, item in enumerate(articles[:5], start=1):
                    if isinstance(item, dict):
                        title = item.get("title", "No title")
                        description = item.get("description", "No description available")

                        speak(f"News {i}. {title}")
                        print(f"Description: {description}\n")

            except requests.exceptions.RequestException as e:
                print("error:", e)
                speak("Sorry I couldn't fetch the news at this moment.")
            
            speak("These are some of the top news headlines for today.")

        elif  "play music" in command or "play song" in command:
            speak("Here you go with your music")
            spotify_url="https://open.spotify.com/"
            open_in_chrome(spotify_url)
            
        elif "send a mail" in command:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("Whom should i send?")
                to = input()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")
        
        elif "time" in command:
            now=datetime.datetime.now()
            hour= now.strftime("%I")
            minute= now.strftime("%M")
            am_pm = now.strftime("%p")
            
            formatted_time = f"{hour}:{minute} {am_pm}"
            speak(f"Sir, the time is {formatted_time}")
            
        elif "where is" in command:
            command = command.replace("where is", "")
            location = command
            speak(f"Locating{location} on google maps")
            open_in_chrome(f"https://www.google.com/maps/place/{location}")
        
        elif "open microsoft edge" in command:
            codePath=r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            os.startfile(codePath)
        
        elif "how are you" in command or "how r u" in command :
            speak(f"I am fine,i hope you are doing well")
            speak(f"so ,how are you sir")

        elif "fine" in command or "good" in command:
            speak(f"Good to see u fine ")
        
        elif "change my name to" in command:
            command=command.replace("change my name to","")
            uname=command
            break

        elif "what's your name" in command or "what is your name" in command:
            speak(f"my friends call me {assname}")
        
        elif "powerpoint" in command:
            speak(f"opening powerpoint")
            powerpoint_path=r'"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"'
            os.system(powerpoint_path)

        elif "who are you" in command:
            speak(f"I am your voice assistant created by Ayan and Sahil")

        elif "reason for you" in command:
            speak(f"i was develop as minor project by Ayan and Sahil")
            
        elif "joke" in command:
            speak(pyjokes.get_joke())
            
        elif "camera" in command or "take a photo" in command:
            speak("Opening Camera app...")
            os.system("start microsoft.windows.camera:")
            
        elif "lock window" in command:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
            
        elif "don't listen" in command or "stop listening" in command:
            speak("for how long you want me to stop listening commands? Please say the number in seconds.")
            a = int(takeCommand())
            speak(f"Okay, pausing for {a} seconds.")
            time.sleep(a)
            
        elif "hibernate" in command or "sleep" in command:
            speak("Hibernating")
            subprocess.call("shutdown /h")
            
            
        elif "shutdown pc" in command or "shutdown laptop" in command:
            speak("Are you sure you want to shut down the system? Please say yes or no.")
            confirm = takeCommand()
            if "yes" in confirm:
                os.system("shutdown /s /t 0")
            else:
                speak("Shutdown Cancelled.")
                
    
        else:
            speak("Give me command so that i can help you")
            if not handle_follow_up():
                break

listening = False

if __name__ == '__main__':
    
    clear = lambda: os.system('cls')

    clear()

    global exit_flag
    exit_flag = False

    wishMe()
    username()
    activate_assistant()

#-------------------------------------------------------