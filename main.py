import sys
from PyQt6.QtWidgets import QApplication, QTextEdit, QLineEdit, QMainWindow, QPushButton
from backend import Chatbot
from threading import Thread

class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setMinimumSize(600, 500)
        # Chat box
        self.chat_box = QTextEdit(self)
        self.chat_box.setGeometry(10, 10, 400, 300)

        # Input box
        self.input_box = QLineEdit(self)
        self.input_box.setGeometry(10, 320, 400, 30)

        # Send button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(420, 320, 50, 30)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_prompt = self.input_box.text()
        self.input_box.clear()
        print(user_prompt)
        self.chat_box.append(f"Me: {user_prompt}")

        chat_thread = Thread(target=self.get_gpt_response, args=(user_prompt,))
        chat_thread.start()

    def get_gpt_response(self, user_prompt):
        response = self.chatbot.get_response_ugpt(user_input=user_prompt)
        self.chat_box.append(f"Bot: {response}")


app = QApplication(sys.argv)
main_window = ChatWindow()
sys.exit(app.exec())
