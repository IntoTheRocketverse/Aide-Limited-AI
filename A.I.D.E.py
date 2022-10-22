import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import date

recognizer = sr.Recognizer()
microphone = sr.Microphone()

engine = pyttsx3.init()
engine.setProperty('volume', 1.0)

WAKE = "Ade"

CONVERSATION_LOG = "Conversation Log.txt"

SEARCH_WORDS = {"who": "who", "what": "what", "when": "when", "where": "where", "why": "why", "how": "how", "is": "is"}

spotify_query = ""

class Ade:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def hear(self, recognizer, microphone, response):
        try:
            with microphone as source:
                print("Waiting for command.")
                recognizer.adjust_for_ambient_noise(source)
                recognizer.dynamic_energy_threshold = 3000
                audio = recognizer.listen(source, timeout=5.0)
                command = recognizer.recognize_google(audio)
                s.remember(command)
                return command.lower()
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Network error.")



    def start_conversation_log(self):
        today = str(date.today())
        today = today
        with open(CONVERSATION_LOG, "a") as f:
            f.write("Conversation started on: " + today + "\n")
    def remember(sef, command):
        with open(CONVERSATION_LOG, "a") as f:
            f.write("User: " + command + "\n")

    def find_search_words(self, command):

        if SEARCH_WORDS.get(command.split(' ')[0]) == command.split(' ')[0]:
            return True

    def analyze(self, command):
        try:

            if self.find_search_words(command):
                s.speak("Here is what I found.")
                webbrowser.open("https://www.google.com/search?q={}".format(command))

            elif command == "open youtube":
                s.speak("Opening Youtube")
                webbrowser.open("https://www.youtube.com")
            elif command == "What is the date today":
                s.speak("it is the " + date)
            elif command == "introduce yourself":
                s.speak("I am Aide, I am an a i software coded in python by two of the youngest coders.")
            elif command == "open twitter":
                webbrowser.open("twitter.com")
                s.speak("Opening twitter, now.")
            elif command == "open google":
                webbrowser.open("https://www.google.com")
                s.speak("Opening google")
            elif command == "open netflix":
                webbrowser.open("https://netflix.com")
            elif command == "open facebook":
                webbrowser.open("https://facebook.com")
                s.speak("opening face book")
            elif command == "open social media":
                s.speak("what media service would you like?")
                if s.hear(recognizer, microphone, response) == "twitter":
                    webbrowser.open("https://www.twitter.com")
                if s.hear(recognizer, microphone, response) == "instagram":
                    webbrowser.open("https://www.instagram.com")
                if s.hear(recognizer, microphone, response) == "facebook":
                    webbrowser.open("https://www.facebook")


            
            else:
                s.speak("I don't know how to do that yet, if you think i do know how, please repeat your sentence. ")
        except TypeError:
            pass

    def listen(self, recognizer, microphone):
        while True:
            try:
                with microphone as source:
                    print("Listening.")
                    recognizer.adjust_for_ambient_noise(source)
                    recognizer.dynamic_energy_threshold = 3000
                    audio = recognizer.listen(source, timeout=5.0)
                    response = recognizer.recognize_google(audio)
                    if response == WAKE:
                        s.speak("How may i help you")
                        return response.lower()
                    else:
                        pass
            except sr.WaitTimeoutError:
                pass
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("Network error")


s = Ade()
s.start_conversation_log()
while True:
    response = s.listen(recognizer, microphone)
    command = s.hear(recognizer, microphone, response)
    s.analyze(command)
