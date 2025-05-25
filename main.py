import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if "kama" in command:
                command=command.replace("kama","")
    except:
        pass
    return command

def run_kama():
    run=1
    while(run):
        command=take_command()
        if "play" in command:
            song=command.replace("play","")
            talk("Playing"+song)
            pywhatkit.playonyt(song)
        elif "time" in command:
            time=datetime.datetime.now().strftime("%I:%M %p")
            talk("The time is "+time)
        elif "who is" in command:
            person=command.replace("who is","")
            info=wikipedia.summary(person,1)
            talk(info)
        elif "date" in command:
            talk("Yessssss! You finally asked me out!")
        elif "are you single" in command:
            talk("Nah man nah! i am with wifi")
        elif "joke" in command:
            talk(pyjokes.get_joke())
        elif "stop" in command:
            talk("Adios! bye bye")
            run=0
        else:
            talk("Pardon me! Could you come again?")
        
if __name__=="__main__":
    print("listening...")
    run_kama()
