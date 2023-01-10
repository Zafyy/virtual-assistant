import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!")   

    else:
        talk("Good Evening!")  

    talk("I am el sir. Please tell me how may I help you")

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'el' in command:
                print(command)
            
                
    except Exception as e:
        talk('please call my name sir')
        take_command()
    return command


def run_el():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
        
    elif 'who is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif 'joke' in command:
        fun = pyjokes.get_joke()
        print(fun)
        talk(fun)

    elif 'whatsapp' in command:
        affan = '+919560811413'
        pywhatkit.sendwhatmsg_instantly(affan, 'hey! how are you?')
    else:
        talk('Please say the command again.')

wishMe()
run_el()