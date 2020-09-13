#Install library yang diperlukan, dan import modulenya
import pyttsx3                      #pip install pyttsx3
import speech_recognition as sr     #pip install speechRecognition
import datetime
import wikipedia                    #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import wolframalpha                 #pip install wolframalpha
from googletrans import Translator  #pip install googletrans

#inisialisasi suara dari library text to speech
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')            #inisialisasi rate
engine.setProperty('rate', 155)              #untuk mengatur kecepatan bicara
engine.setProperty('voice', voices[0].id)    #voices[1].id untuk suara wanita

#define fungsi speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#define fungsi wishMe
def wishMe():
    print("\n================== System Activated ==================")
    speak("System Activated")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("\nGood Morning")
        speak("Good Morning... !")

    elif hour>=12 and hour<18:
        print("\nGood Afternoon")
        speak("Good Afternoon... !")   

    else:
        print("\nGood Evening")
        speak("Good Evening... !")  

    print("Hello Sir, I am E-Tron your personal assistant\n")
    speak("Hello Sir, I am E-Tron your personal assistant !")
    speak("I can help you do some task for your studying... Please let me know what did you want to do for Today ?")       

def takeCommand():
    #Input diambil dari mikrofon pengguna kemudian disimpan sebagai output string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nE-Tron : I will listen to your orders...")
        speak("I will listen to your orders...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
    try:
        print("\nNow Recognizing...")    
        query = r.recognize_google(audio, language='en-ID')
        print("User said:",query)

    except Exception as e:
        #print(e)    
        print("\nE-Tron : Say that again please...\n")
        speak("Say that again please...")
        print("\n++++++ System Return ++++++\n")  
        return "None"
    return query

#define module untuk setting SMTP client session dengan port TLS 587
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('azkaa6626@gmail.com', 'qwerty@1234')
    server.sendmail('azkaa6626@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if logika 1:
        query = takeCommand().lower()

        # logika untuk eksekusi task berdasarkan query
        if 'how are you' in query:
            speak("i am fine sir, thank you for asking, how about you sir ?")

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            speak(query)
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print("\n", results)
            speak(results)

        elif 'youtube' in query:
            url = 'https://www.youtube.com/results?search_query='
            speak('Searching Youtube...')
            query = query.replace("youtube", "")
            speak(query)
            webbrowser.get().open_new(url + query)

        elif 'google' in query:
            url = 'https://www.google.com/search?q='
            speak('Searching Google...')
            query = query.replace("google", "")
            speak(query)
            webbrowser.get().open_new(url + query)

        elif 'academy' in query:
            webbrowser.open("http://siakad.untirta.ac.id/portal/")   

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Compact\\Desktop\\EXAMPLE_BOT\\Music' 
            songs = os.listdir(music_dir)
            query = query.replace("play music", "")
            play = random.choice(songs)
            print("\nNow Playing: ", play)    
            os.startfile(os.path.join(music_dir, play))

        elif 'start movie' in query:
            movie_dir = 'C:\\Users\\Compact\\Desktop\\EXAMPLE_BOT\\Movie' 
            video = os.listdir(movie_dir)
            query = query.replace("start movie", "")
            play = random.choice(video)
            print("\nNow Starting: ", play)    
            os.startfile(os.path.join(movie_dir, play))

        elif 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is {strTime}")
            print("\nTIME", strTime)

        elif 'microsoft word' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(codePath)

        elif 'inform' in query:
            app_id = "K9XRK9-5647YVAQRX" 
            client = wolframalpha.Client(app_id) 
  
            indx = query.lower().split().index('inform') 
            query = query.split()[indx + 1:] 
            res = client.query(' '.join(query)) 
            answer = next(res.results).text 
            speak("The answer is " + answer)
            print("\nThe answer is : " + answer)
        
        elif 'translate' in query:
            trans = Translator()
            speak ("Do you want to translate?")
            query = takeCommand()
            t = trans.translate(
                query, src='en', dest='id'
                )
            print(f'ENGLISH : {t.origin}')
            print(f'INDO : {t.text}')
            print(f'{t.origin} ===> {t.text}')

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "maulana.zensih2016@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
                print("\nEmail has been sent!")

            except Exception as e:
                print(e)
                speak("Sorry Sir, i can't be able to send the email, please try again sir")    