from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys 
import DatabaseApi


class show_Dataset(QWidget):
    def __init__(self, parent=None):
        super(show_Dataset, self).__init__(parent)
        self.resize(500, 600)
        self.setWindowTitle("Role dataset")
        self.setFixedHeight(300)
        self.setFixedWidth(600)
        self.adjustSize()
        # fonts
        font = QFont()
        font.setBold(True)
        font.setCapitalization(True)
        font.setPointSize(13)
        # header
        self.label = QLabel(self)
        self.label.setText("counts: ")
        self.label.move(110,50)
        self.label.setFont(font)
        self.label.setFixedHeight(30)
        self.label.setFixedWidth(170)
        self.label.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")

        self.label1 = QLabel(self)
        self.label1.setText("type of material:")
        self.label1.move(110,100)
        self.label1.setFont(font)
        self.label1.setFixedHeight(30)
        self.label1.setFixedWidth(170)
        self.label1.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")

        self.label = QLabel(self)
        self.label.setText(self.count())
        self.label.move(300,50)
        self.label.setFont(font)
        self.label.setFixedHeight(30)
        self.label.setFixedWidth(170)
        self.label.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")

        self.label1 = QLabel(self)
        #self.label1.setText(self.material())
        self.label1.move(300,100)
        self.label1.setFont(font)
        self.label1.setFixedHeight(30)
        self.label1.setFixedWidth(170)
        self.label1.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")

    def count(self):
        while True:
            inptt = input('scan qr')
            out = DatabaseApi.DatabaseApi.fetch(inptt)
            return str(out['count'])

    # def material(self):
    #     DatabaseApi.parse



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app1 = show_Dataset()
    app1.show()
    sys.exit(app.exec())
        