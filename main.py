import sys
from PyQt6.QtWidgets import QApplication, QTextEdit, QMainWindow, QPushButton


class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600, 500)
        # Chat box
        self.chat_box = QTextEdit(self)
        self.chat_box.setGeometry(10, 10, 400, 300)

        # Input box
        self.input_box = QTextEdit(self)
        self.input_box.setGeometry(10, 320, 400, 30)

        self.button = QPushButton("Send", self)
        self.button.setGeometry(420, 320, 50, 30)

        self.show()




app = QApplication(sys.argv)
main_window = ChatWindow()
sys.exit(app.exec())
