import speech_recognition as sr
import pyttsx3
import webbrowser
import musiclibrary as ml
import requests
tts=pyttsx3.init()# it is used to convert text into speech, so we first initialize it
api_key = 'a7cb5e02387f4391a8fd536d69679727'
url = (f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={api_key}")
def speak(text):
   tts.say(text)# it will say text that u will send to him
   tts.runAndWait()# it is neccessary 
# this will process the command on webbrowser
def processcommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   
   elif "open youtube" in c.lower():
      webbrowser.open("https://www.youtube.com/")
   
   elif "open facebook" in c.lower():
      webbrowser.open("https://www.facebook.com/")
   
   elif "open linkedin" in c.lower():
      webbrowser.open("https://www.linkedin.com/feed/")
   
   elif "open spotify" in c.lower():
      webbrowser.open("https://open.spotify.com/collection/tracks")
   
   elif (c.lower().startswith("play")):
      song=c.lower().split(" ")[1]
      link=ml.music[song]
      webbrowser.open(link)
   
   elif "news"in c.lower():
      # Send a GET request to the News API
      response = requests.get(url)
      # Check if the request was successful
      if response.status_code == 200:
         # Parse the JSON response
         data = response.json()
         
         # Check if the response contains articles
         articles = data['articles',[]]
            
            # Extract and print publication dates
         for article in articles:
            speak(article["title"])
            

# it is a good practice to do this if we are working on imported packages
if (__name__=="__main__"):
   speak("jarvis initializing .......")
   while True:
      r=sr.Recognizer()# the object is being made of voice recognizer
      # always try to write code in try except so that it won't throw an error 
      try:
         with sr.Microphone() as source:
          print("listening....")
          audio=r.listen(source,timeout=3,phrase_time_limit=1)
         word=r.recognize_google(audio)# we actually use google recognizer as audio to speech 
         print("recognising...")
         print(word)# it is used to print what we actually spoke
         if (word.lower()=="jarvis"):
            speak("ya")
            # listen for command
            with sr.Microphone() as source:
                print("jarvis Activate...")
                audio=r.listen(source)
                command=r.recognize_google(audio)
                print(command)
                processcommand(command)
        
        
      except Exception as e:
         print(e)