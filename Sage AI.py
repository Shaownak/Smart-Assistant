import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import spotify

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                print(command)
                command = command.replace("alexa","")
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%H %p')
        print(time)
        talk("Current time is " + time)
    elif "play" in command:
        song = command.replace("play","")
        print(song)
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif "what is" or "tell me about" in command:
        look_for = command.replace("what is" or "tell me about", "")
        info = wikipedia.summary(look_for,1)
        print(info)
        talk(info)
    elif "play on spotify" in command:
        song = command.replace("play on spotify", "")
        print(song)
        talk("playing " + song + " on spotify")
        spotify.track(song)
    elif "who are you" in command:
        talk("I am Alexa")



run_alexa()
