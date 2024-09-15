MEGA PROJECT 1: Jarvis - Voice-Activated Virtual Assistant
<br>
Jarvis is a sophisticated voice-activated virtual assistant, designed to streamline everyday tasks such as web browsing, playing music, fetching news, and responding to user queries using OpenAI's GPT-3.5-turbo model. It is built to handle voice commands and provide intelligent, real-time responses, making it a helpful personal assistant similar to Alexa or Google Assistant.
<br>
<br>
Features:

Voice Recognition: Utilizes the speech_recognition library to listen for voice commands and activates when it detects the wake word "Jarvis."
<br>
<br>
Text-to-Speech: Converts text to speech using pyttsx3 for local conversion or gTTS (Google Text-to-Speech) for higher-quality responses, with playback managed by pygame.
<br>
<br>
Web Browsing: Opens popular websites like Google, YouTube, Facebook, and LinkedIn through simple voice commands.
<br>
<br>
Music Playback: Interfaces with a custom musicLibrary module to play songs via web links.
<br>
<br>
News Fetching: Fetches and reads the latest news headlines using the NewsAPI.
<br>
<br>
OpenAI Integration: Leverages OpenAI's GPT-3.5-turbo to handle complex user queries, generating informative and accurate responses.
Workflow
<br>
<br>
Initialization: Starts by greeting the user with "Initializing Jarvis…".
<br>
<br>
Wake Word Detection: Listens for the wake word "Jarvis" and activates upon detection.
<br>
<br>
Command Processing: Processes various user commands for tasks such as web browsing, playing music, fetching news, or generating AI-powered responses.
<br>
<br>
Speech Output: Delivers responses using either pyttsx3 or gTTS for speech output.
<br>
<br>
Libraries Used:
<br>
<br>
speech_recognition
<br>
webbrowser
<br>
pyttsx3
<br>
musicLibrary
<br>
requests
<br>
openai
<br>
gTTS
<br>
pygame
<br>
os
