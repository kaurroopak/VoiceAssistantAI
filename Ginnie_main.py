import pyttsx3
import speech_recognition
import datetime
import pyautogui
import pyjokes
import randfacts
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak(" Jo hukam mere aakaa , You can me call anytime")
                    break

                elif "hello" in query:
                    speak("Hello , how are you ?")
                elif "i am fine" in query or "i am good" in query:
                    speak("That's great, aakaa")
                elif "what" and "about you" in query:
                    speak("I am also having a good day")
                elif "how are you" in query:
                    speak("I am good aaka, how are you ?")
                elif "thank you" in query:
                    speak("you are welcome, always there for you anytime")
                elif "define yourself" in query:
                    speak("I am an Assistant, Your Assistant Ginnie"
                          "I am here to make your life easier"
                          "You can command me to perform various tasks such as asking questions "
                          "or opening applications etcetera")
                elif "your name" in query:
                    speak("My name is Ginnie")
                elif"why do you exist" in query:
                    speak("It's a secret aakaa")
                elif "calculations" in query or "help me" in query:
                    speak("Sure aakaa, i can help you in some basic arithmetic calculations like addition, subtraction, multiplication and division")

                elif "play a game" in query:
                    from Game import game_play
                    game_play()

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "google" in query:
                    from SearchWeb import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from SearchWeb import searchYoutube
                    searchYoutube(query)

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

                elif "wikipedia" in query:
                    from SearchWeb import searchWikipedia
                    searchWikipedia(query)

                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

                elif "temperature" in query or "weather" in query:
                    from Weather import *
                    print("Temperature in Patiala is " + str(temp()) + " degree celsius and with "+ str(des()))
                    speak("Temperature in Patiala is " + str(temp()) + " degree celsius and with "+ str(des()))

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"The time right now is {strTime}")
                    print(f"The time right now is {strTime}")

                elif "calculate" in query:
                    from Calculator import Calc
                    query = query.replace("calculate", "")
                    query = query.replace("ginnie", "")
                    Calc(query)

                elif "coding related" in query:
                    speak("Get ready for some chuckles")
                    joke = pyjokes.get_joke()
                    speak(joke)
                    print(joke)

                elif "funny" in query or "joke" in query:
                    from Jokes import jokes
                    speak("Sure, get ready for some chuckles")
                    arr = jokes()
                    print(arr[0])
                    speak(arr[0])
                    print(arr[1])
                    speak(arr[1])

                elif "fact" in query:
                    speak("sure, ")
                    x = randfacts.get_fact()
                    print(x)
                    speak("Did you know that, " + x)

                elif "screenshot" in query:
                    import pyautogui
                    im = pyautogui.screenshot()
                    im.save(r"C:\Users\DELL\Pictures\Screenshots\ss.png")

                elif "click my photo" in query or "camera" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")

                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break

                elif "finally sleep" in query:
                    speak("Jo hukam mere aakaa")
                    speak("Going to sleep")
                    exit()

