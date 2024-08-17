import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said : {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def game_play():
    speak("Lets Play ROCK PAPER SCISSORS !!")
    print("LETS PLAYYYYYYYYYYYYYY")
    i = 0
    Me_score = 0
    Comp_score = 0
    while (i < 5):
        choose = ("rock", "paper", "scissors")  # Tuple
        comp_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
            if (comp_choose == "rock"):
                speak("ROCK")
                print(f"Score:- ME :- {Me_score} : COMP :- {Comp_score}")
            elif (comp_choose == "paper"):
                speak("paper")
                Comp_score += 1
                print(f"Score:- ME :- {Me_score} : COMP :- {Comp_score}")
            else:
                speak("Scissors")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COMP :- {Comp_score}")

        elif (query == "paper"):
            if (comp_choose == "rock"):
                speak("ROCK")
                Me_score += 1
                print(f"Score:- ME :- {Me_score + 1} : COMP :- {Comp_score}")

            elif (comp_choose == "paper"):
                speak("paper")
                print(f"Score:- ME :- {Me_score} : COMP :- {Comp_score}")
            else:
                speak("Scissors")
                Comp_score += 1
                print(f"Score:- ME :- {Me_score} : COMP :- {Comp_score}")

        elif (query == "scissors" or query == "scissor"):
            if (comp_choose == "rock"):
                speak("ROCK")
                Comp_score += 1
                print(f"Score:- ME :- {Me_score} : COMP :- {Comp_score}")
            elif (comp_choose == "paper"):
                speak("paper")
                Me_score += 1
                print(f"Score:- ME :- {Me_score} : COMP :- {Comp_score}")
            else:
                speak("Scissors")
                print(f"Score:- ME :- {Me_score} : COMP :- {Comp_score}")

        elif (query == "quit"):
            break
        i += 1

    print(f"FINAL SCORE :- ME :- {Me_score} : COMP :- {Comp_score}")
