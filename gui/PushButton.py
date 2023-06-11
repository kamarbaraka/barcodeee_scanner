import sys
from PyQt6.QtWidgets import QWidget, QLabel, QApplication, QPushButton
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    """
    main window class
    """

    name_label = ''
    button = ''
    times_pressed = 0

    def __init__(self):
        super().__init__()
        self.initializer()

    def initializer(self):
        self.setWindowTitle('push button')
        self.setGeometry(100, 100, 400, 400)

        self.setUpindow()

        self.show()

    def setUpindow(self):
        """
        method to set up the main window
        :return: void
        :param: self
        """

        name_label = QLabel('don"t press the button', self,)
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.move(60, 30)
        self.name_label = name_label

        button = QPushButton('click me', self)
        button.move(80, 70)
        self.button = button
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        self.times_pressed += 1

        match self.times_pressed:
            case 1:
                self.name_label.setText('why did you click me')
            case 2:
                self.name_label.setText('i"m warning you')
                self.button.setText('feeling lucky?')
                self.button.adjustSize()
                self.button.move(70, 70)
            case 3:
                print('window closed')
                self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
