import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyaudio 
import pywhatkit
import pyjokes
import pyautogui
# from send_mail import sendEmail
# import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)   
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")

    speak("I am jarvis. Please tell me how may I help you")             


def takeCommand():
    #it takes microphone input from user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)   
        print("say that again")
        return "None"  

    return query   


if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        #logic for executing task

        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'play' in query:
            song = query.replace('play','')
            speak('playing' + song)
            pywhatkit.playonyt(song) 

        elif 'open geeksforgeeks' in query:
            speak("Opening GeeksforGeeks ")
            webbrowser.open("www.geeksforgeeks.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")  

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'tell me a joke' in query:
            speak(pyjokes.get_joke())      

        elif 'play music' in query:
            webbrowser.open("spotify.com")

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")  

        elif 'open code' in query:
            codePath="C:\\Users\\ADITI SAHU\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'volume up' in query:
            pyautogui.press('volumeup')

        elif 'volume down' in query:
            pyautogui.press('volumedown')

        elif 'volume mute' in query or 'mute' in query:
            pyautogui.press('volumemute')    

        else:
            speak("please say the command again")    


        if 'quit' in query:
            speak("Bye maam have a nice day.")
            exit()        


