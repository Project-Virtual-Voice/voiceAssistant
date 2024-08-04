import pyttsx3
import datetime

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Retrieve available voices
voices = engine.getProperty('voices')
# Print available voices for debugging
for voice in voices:
    print(f"Voice ID: {voice.id}, Name: {voice.name}")

# Set the voice (ensure the index matches an available voice)
engine.setProperty('voice', voices[0].id)  # Adjust index if needed

def speak(audio):
    """Convert text to speech."""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Greet based on the time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon")
    elif hour >= 17 and hour < 20:
        speak("Good Evening")
    else:
        speak("Good Night")

if __name__ == "__main__":
    wishMe()
