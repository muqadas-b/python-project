import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():  
    global instruction        
    try:
        with sr.Microphone() as origin:
            print("Listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace("jarvis", "").strip()
                print("Command:", instruction)
                return instruction
           
    except:
        pass
    return instruction
def play_jarvis():

    instruction = input_instruction()
    print(instruction)
    if "play" in instruction:
        song = instruction.replace("play", "").strip()
        talk("Playing " + song)
        pywhatkit.playonyt(song)

    elif "time" in instruction:
         time = datetime.datetime.now().strftime("%I:%M %p")
         talk("Current time is " + time)
    elif "date" in instruction:
         date = datetime.datetime.now().strftime("%d / %m / %Y")
         talk("Today's date is " + date)
    elif "how are you" in instruction:
         talk("I am fine, how about you?")

    elif "what is your name" in instruction:
         talk("I am Jarvis. What can I do for you?")

    elif "who is" in instruction:
         try:
            person = instruction.replace("who is", "").strip()
            info = wikipedia.summary(person, sentences=2)
            print(info)
            talk(info)
         

         except:
            talk("sorry,i could not find that person")

    else:
        talk("Please repeat that.")
# Run jarvis
play_jarvis()

