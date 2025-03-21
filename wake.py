import speech_recognition as sr
import os

def listen_for_wake_word():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for 'Hello Jarvis' to activate the assistant...")
        
        while True:
            try:
                print("Waiting for wake word...")
                audio = recognizer.listen(source)
                
                command = recognizer.recognize_google(audio).lower()
                
                print("You said:", command)
                
                if "hello" in command:
                    print("Wake word detected! Starting  assistant...")
                    os.system("python assistant.py")
                    break
                
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError:
                print("Speech Recognition service error.")
                break
            
if __name__ == "__main__":
    listen_for_wake_word()