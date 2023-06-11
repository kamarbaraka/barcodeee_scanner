import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPixmap, QFont


class UserProfile(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('User Profile')
        self.setGeometry(100, 100, 400, 600)

        self.setUp()

        self.show()

    def setUp(self):
        self.setUpImages()

        user_label = QLabel(self)
        user_label.setText('Kamar Baraka')
        user_label.setFont(QFont('Arial', 20))
        user_label.move(80, 140)

        bio_label = QLabel(self)
        bio_label.setText('Biography')
        bio_label.setFont(QFont('Arial', 17))
        bio_label.move(10, 170)

        about_label = QLabel(self)
        about_label.setText('I"m a software developer')
        about_label.move(10, 190)

    def setUpImages(self):

        profile_picture = r"C:\Users\kamar\Pictures\kbhacksicon.png"
        background_picture = r"C:\Users\kamar\Pictures\EIE Projects List for Final Year Engineering Engineering Students.jpg"
        picture_list = [background_picture, profile_picture]

        for picture in picture_list:
            try:
                with open(picture):
                    picture_label = QLabel(self)
                    pixmap = QPixmap(picture)
                    picture_label.setPixmap(pixmap)

                    if picture == profile_picture:
                        picture_label.setGeometry(0, 0, 100, 50)
                        #picture_label.move(20, 40)
                    picture_label.setGeometry(0, 0, 1000, 200)
            except FileNotFoundError:
                print(f'error: {FileNotFoundError}')


if __name__ == '__main__':
    app = QApplication([])
    window = UserProfile()
    sys.exit(app.exec())
