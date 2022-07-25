from webbrowser import get
import speech_recognition as sr
from gtts import gTTS
import random
import os
import playsound
from datetime import datetime

r = sr.Recognizer()

def getTime():
    now = datetime.now()
    currentTime = now.strftime("%H:%M %p")
    return currentTime

def greeting():
    currentTime = datetime.now()
    if currentTime.hour < 12:
        return "morning"
    elif currentTime.hour > 12 and currentTime.hour < 16:
        return "afternoon"
    else:
        return "evening"

def bhimaSpeech(voiceData):
    tts = gTTS(text=voiceData, lang="en")
    r = random.randint(1, 10000000)
    audioFile = 'audio-' + str(r) + '.mp3'
    tts.save(audioFile)
    os.system("play " + audioFile + " tempo 1.25")
    print(voiceData)
    os.remove(audioFile)

def recordAudio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voiceData = ''
        try:
            voiceData = r.recognize_google(audio)
            print(voiceData)
        except sr.UnknownValueError:
            bhimaSpeech("Sorry, I didn't recognize what you said.")
        except sr.RequestError:
            bhimaSpeech("Sorry, Technical Error")
        return voiceData

def respond(voiceData):
    match voiceData:
        case "who are you":
            bhimaSpeech("Bhima")
    
        case "what's the time":
            bhimaSpeech(getTime())
        
        case "stop":
            bhimaSpeech("Goodbye")
            exit()

bhimaSpeech(("Good {}").format(greeting()))
while True:
    voiceData = recordAudio()
    respond(voiceData)
