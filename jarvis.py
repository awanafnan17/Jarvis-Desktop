import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
from googlesearch import search
import smtplib




emails = {'me': 'awanafnan17@gmail.com'}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon!")
    elif hour>=17 and hour<19:
        speak("Good Evening!")
    elif hour>=19 and hour<25:
        speak("Good Night!")
    elif hour>=0 and hour<5:
        speak("Good Night!")
    speak("Hi I am Jarvis. How may I help you!")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1.4
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-pak')
        print(f"User said: {query}")

    except Exception as e:
        print(e)
        print('Say that again please!')
        return 'None'
    return query

def sendEmail(to, cont):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("Your email", "Your pass")
    server.sendmail("Your email", to, cont)
    server.close()


if __name__=="__main__":
    wishMe()
    speak('Sir, You can ask what the time from me, you can get me to up any .com website using website.com, you can search wikipedia by speaking the name of search and adding wikipedia at the end, you can also send emails and exit using exit command.')
    while True:
        query = listen().casefold()
        if 'wikipedia' in query:
            speak("Searching Wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            # print(results)
            speak(results)

        elif '.com' in query:
            webbrowser.open(f'https://www.{query}')
            speak(f"Here is your result for {query}")

        elif 'search' in query:
            query = query.replace("search", "")
            for j in search(query, tld="com", num=10, stop=3, pause=2):
                webbrowser.open(j)
            speak(f"Here are your results for {query}")

        elif 'play music' in query:
            musicDir = 'C:\\Users\\Afnan Awan\\Music\\songs'
            songs = os.listdir(musicDir)
            # print(songs)
            randSong = random.randint(0, len(songs))
            os.startfile(os.path.join(musicDir, songs[randSong]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, The Time is {strTime}")

        elif 'open code' in query:
            vsPath = "C:\\Users\\Afnan Awan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsPath)

        elif 'send email' in query:
            try: 
                speak('What should I say?')
                cont = listen()
                speak('To whom should I send this?')
                to = listen().casefold()
                if to in emails:
                    sendEmail(emails[to], cont)
                    speak('your email has been sent!')
                else:
                    speak('Name not found!')
            except Exception as e:
                print(e)
                speak('Sorry my friend, I could not send the email!')
        

        elif 'exit' in query:
            speak('As up your request I am shutting myself down!')
            exit()