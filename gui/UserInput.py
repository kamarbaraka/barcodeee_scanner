import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt6.QtCore import Qt


class InputWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        self.setMaximumSize(500, 250)
        self.setWindowTitle('User Input')

        self.setUpWindow()

        self.show()

    def setUpWindow(self):
        input_tag = QLabel('please enter your name', self)
        input_tag.move(50, 0)
        input_tag.setAlignment(Qt.AlignmentFlag.AlignCenter)

        name_tag = QLabel('Name', self)
        name_tag.setAlignment(Qt.AlignmentFlag.AlignLeft)
        name_tag.move(0, 50)

        self.line_edit = QLineEdit(self)
        self.line_edit.resize(275, 20)
        self.line_edit.move(50, 50)

        clear_button = QPushButton('clear', self)
        clear_button.move(170, 70)
        clear_button.clicked.connect(self.clearText)

        accept_button = QPushButton('ok', self)
        accept_button.move(250, 70)
        accept_button.clicked.connect(self.acceptText)

    def clearText(self):
        """
        clear the text
        :return: void
        """
        self.line_edit.clear()

    def acceptText(self):
        """
        accept text
        :return: void
        """
        print(self.line_edit.text())
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InputWindow()
    sys.exit(app.exec())
