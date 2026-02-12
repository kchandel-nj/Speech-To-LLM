# Libraries
from google import genai

# Class
class Prompter:
    
    def __init__(self):

        """
        Docstring for __init__

        Initializes the Gemini client and model for prompting.
        
        :param self: Description
        """

        self.client = genai.Client()
        self.GEMINI_MODEL = "gemini-3-flash-preview"
    
    def prompt(self, prompt: str):

        """
        Docstring for prompt

        Feeds the Gemini client the provided prompt and returns the response.
        
        :param self: The object
        :param prompt: The prompt to feed the client.
        :type prompt: str
        :return: The response of the client.
        :rtype: str
        """

        return self.client.models.generate_content(
            model=self.GEMINI_MODEL, contents=prompt
            ).text