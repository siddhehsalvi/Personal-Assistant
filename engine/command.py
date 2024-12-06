import time
import pyttsx3
import speech_recognition as sr
import eel

def Speak(text):
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.setProperty('rate',150)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()


def takecommand():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("listening......")
        eel.DisplayMessage("listening......")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio=r.listen(source, 10, 10)

    try:
        print("recognizing......")
        eel.DisplayMessage("recognizing......")
        query=r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def AllCommands():
    query=takecommand()

    if "open" in query:
        from engine.features import openCommand 
        openCommand(query)
    elif "on youtube":
        from engine.features import playYoutube
        playYoutube(query)
    
    else:
        print("not run")
    
    eel.ShowUi()



