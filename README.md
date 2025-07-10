# 🗣️ Voice Assistant – Final Year Project

A desktop-based voice assistant built in Python as our final year project by Ayan Shaikh and Sahil Patel.

This assistant takes voice (or typed) commands to perform useful tasks like opening websites, fetching info from Wikipedia, telling the time, telling jokes, sending emails, and even shutting down the PC.
It also integrates the Gemini AI API, so users can ask any AI-powered questions directly through the assistant.


---

# ✨ Features

🎤 Voice & text input: Choose to type or speak your commands

📺 Open websites: YouTube, Google, Stack Overflow, and custom search queries

📚 Wikipedia integration: Fetch and read summaries aloud

📧 Send emails through voice commands

📰 Get latest news headlines

🕰️ Tell the current time

🗺️ Locate places on Google Maps

🔒 Lock, shutdown, hibernate or put your PC to sleep

🤖 Ask AI: Integrated with Gemini AI API for AI-generated answers

😂 Tell jokes with PyJokes

📸 Take a photo using your camera

🎵 Play music by opening Spotify

💬 Interactive follow-up: Ask if you want anything else after completing a task

🖥️ Simple CLI interface with voice feedback



---

# 🛠 Tech Stack

Programming Language: Python

Libraries:

pyttsx3 – text-to-speech

speech_recognition – speech to text

wikipedia – fetch summaries

webbrowser, os, subprocess – system and browser automation

requests – for APIs (e.g., news)

google.generativeai – Gemini AI integration

pyjokes – jokes

ctypes – lock workstation

ecapture – capture photo from camera


APIs: Gemini AI, GNews



---

# 🚀 Getting Started

Follow these steps to run the voice assistant locally:

Clone the repository
git clone https://github.com/YourUsername/VoiceAssistant.git

Navigate to the project directory
cd VoiceAssistant

(Optional) Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

Install required packages
pip install -r requirements.txt

Set up your Gemini API key
export GEMINI_API_KEY='your_gemini_api_key'   Windows (CMD): set GEMINI_API_KEY=your_gemini_api_key

Run the assistant
python main.py

✅ On first run, it will ask you to choose input method:

Type commands manually, or

Speak commands using your microphone



---

# 🔑 Environment Variables

Make sure to set these in your environment:

GEMINI_API_KEY – your Gemini AI API key


(You may also add newsapi key in the code if you want to use your own news API.)


---


# 🤝 Authors

Project built as final year project by:

Ayan Shaikh – @Ayan004

Sahil Patel



---

# ⭐ Show your support

If you like this project, please ⭐ the repo!
It helps others discover it and motivates us to keep improving.


---

# 📄 License

This project is open source and available under the MIT License.


---