# Libraries
from GeminiPrompter import Prompter
import pyttsx3

# Initialize
jarvis = Prompter()
engine = pyttsx3.init()

try:
    answer = jarvis.prompt("Hello, Gemini!")
    print(answer)
    engine.say(answer)
    engine.runAndWait() # Stops the program until speech is completed
except:
    engine.say("Error")
    engine.runAndWait()
print("Done")