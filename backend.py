import os
import openai


class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv("OPEN_AI_API_KEY")

    def get_response(self, user_input):
        response = openai.ChatCompletion.create(
            model="text-davinci-001",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == '__main__':
    chatbot = Chatbot()
    reply = chatbot.get_response("Tell a joke.")
    print(reply)
