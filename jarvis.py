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
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            instruction = listener.recognize_google(voice)
            instruction = instruction.lower()

            if "jarvis" in instruction:
                instruction = instruction.replace("jarvis", "").strip()
                print("Command:", instruction)
                return instruction
    except:
        pass

    return ""

def play_Jarvis():
    instruction = input_instruction()
    print("You said:", instruction)

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
        person = instruction.replace("who is", "").strip()
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    else:
        talk("Please repeat that.")

# Run Jarvis
play_Jarvis()
