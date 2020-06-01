import pyttsx3 
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #0 for boy , 1 for girl



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print('Morning is good!')
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print('Good Afternoon!')
        speak("Good Afternoon!")   

    else:
        print('Good Evening!')
        speak("Good Evening!")  

    print("I am Spyron A I . Please tell me how may I help you")
    speak("I am Spyron A I . Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'item in  google' in query:
            speak('Searching google...')
            query = query.replace("google", "")
            results = webbrowser.open(query)
            speak("wait sir")
            speak(results)
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'open code' in query:
            codePath = "F:\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        elif 'open google chrome' in query:
            chromepath='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk'
            os.startfile(chromepath)
        
        elif  "how are you" in query:
            speak("I am fine. how about you")
        
         
        elif 'quit' in query:
            speak("ok sir")
            break        
        elif 'wait' in query:
            speak("ok sir")
            time.sleep(10)
        elif 'are you listening' in query:
            speak("always sir")
        elif 'tell me something about yourself' in query:
            credits="I am built by Hemant."
            print(credits)
            speak(credits)
        elif 'hello' in query:
            greets="Hi sir. How's your day "
            print(greets)
            speak(greets)
        else:
            speak("command not recognised")
