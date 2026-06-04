# Libraries
from GeminiPrompter import Prompter
from CommandInterface import Command

class SpeechApparatus:

    def __init__(self):
        # Initialize
        self.jarvis = Prompter()

    def prompt(self, text: str) -> str:
        try:
            answer = self.jarvis.prompt(text)
            print(answer)
            return answer
        except:
            print("Error")
            return "Error"

speaker = SpeechApparatus()
interpreter = Command()
GEMINI_INSTRUCTIONS = "You are playing the role of a home assistant, akin to an Alexa. " \
"Following these instructions, you will be given a user-written command. " \
"If the command is something that uses capability built into your engine, you may just return a response approrpiate to you. " \
"If you are given a command that you cannot execute, return it in a specific format supplied here." \
"You must interpret these commands in accordance to the commands I supply to you now: " \
"1. Turn on specified lights " \
"2. Turn off specified lights " \
"Return ONLY text with the command in this specific format: 'number:(arg1,arg2,arg3,...)' " \
"The command will now be provided to you: "

while True:
    cmd = input("Enter command: ")
    command = speaker.prompt(GEMINI_INSTRUCTIONS + cmd)
    interpreter.interpret_command(str(command))