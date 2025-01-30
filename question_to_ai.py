import ollama
client = ollama.Client()


defaultPrompt = """Act as a Wordle-solving assistant. I will provide you with feedback from the Wordle game after each guess, and you will suggest the next 5-letter word to try. The feedback will be in the format: X O O X Y, where:

X means the letter is not in the target word.

O means the letter is in the correct position.

Y means the letter is in the word but in the wrong position.

Your responses must always be a valid 5-letter word. Do not provide any explanations or additional text—only the word.

The first word attempp will always be "stone", hardcoded.
Let’s begin. The feedback is:
 """

class QuestionToAI:
    def __init__(self):
        self.client = ollama.Client()
        self.model = "llama3.2"

    def ask(self, question):
        response = self.client.generate(model=self.model, prompt=defaultPrompt + question)
        return response.response