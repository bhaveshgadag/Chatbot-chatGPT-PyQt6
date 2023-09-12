import os, sys
import openai
from UnlimitedGPT import ChatGPT
sys.path.append("..")
from globalvars import get_session_token, get_conversation_id


class Chatbot:
    def __init__(self):
        openai.api_key = os.getenv("OPEN_AI_API_KEY")
        self.session_token = get_session_token()
        self.conversation_id = get_conversation_id()

    def get_response(self, user_input):
        response = openai.ChatCompletion.create(
            model="text-davinci-001",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response

    def get_response_ugpt(self, user_input):
        print(self.session_token)
        print(self.conversation_id)
        chatbot_ugpt = ChatGPT(
            self.session_token,
            conversation_id=self.conversation_id,
            proxy=None,
            chrome_args=[],
            disable_moderation=False,
            verbose=True
        )
        message = chatbot_ugpt.send_message(
            user_input,
            input_mode="SLOW",  # Can be INSTANT or SLOW
            input_delay=1
        )
        return message.response


if __name__ == '__main__':
    chatbot = Chatbot()

    # Quota limit exceeded on openai
    # reply = chatbot.get_response("Tell a joke.")
    # print(reply)

    # Using alternative - UnlimitedGPT, headless does not work
    response = chatbot.get_response_ugpt("tell an indian joke.")
    print("printing response")
    print(response)



