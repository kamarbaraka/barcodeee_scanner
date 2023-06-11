import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.__initializer()

    def __initializer(self):
        self.setWindowTitle('Main Window')
        self.setGeometry(200, 100, 500, 500)
        self.imageDisplay()
        self.show()

    def imageDisplay(self):
        hello_text = QLabel(self)
        hello_text.setText('check this out')
        hello_text.move(200, 0)

        image = r"C:\Users\kamar\Pictures\kbhacksicon.png"

        with open(image):
            image_label = QLabel(self)
            pixmap = QPixmap(image)
            image_label.setPixmap(pixmap)
            print(image_label.geometry())


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    sys.exit(app.exec())
