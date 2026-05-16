# Libraries
from GeminiPrompter import Prompter
import pyttsx3

class SpeechApparatus:

    def __init__(self):
        # Initialize
        self.jarvis = Prompter()
        self.engine = pyttsx3.init()

    def prompt(self, text: str):
        try:
            answer = self.jarvis.prompt("Hello, Gemini!")
            print(answer)
            self.engine.say(answer)
            self.engine.runAndWait() # Stops the program until speech is completed
        except:
            self.engine.say("Error")
            self.engine.runAndWait()
        print("Done")