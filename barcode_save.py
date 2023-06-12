# import EAN13 from barcode module
from barcode import *
import random
  
# import ImageWriter to generate an image file
from barcode.writer import ImageWriter

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys 
import changes.changes

class show_Dataset22(QWidget):
    count = 0
    def __init__(self , parent=None):
        super(show_Dataset22, self).__init__(parent)
        self.resize(500, 600)
        self.setWindowTitle("barcode generator")
        # self.setStyleSheet("background-image: url(12.png);")
        self.setFixedHeight(300)
        self.setFixedWidth(600)
        self.setWindowIcon(QIcon('./images/logo.png'))
        # Create a label widget and set its background image
        pixmap = QPixmap('./images/13.png')
        self.background_label = QLabel(self)
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, 640, 480)
        self.background_label.setFixedHeight(1000)
        self.background_label.setFixedWidth(1500)

        # fonts
        font = QFont()
        font.setBold(True)
        font.setCapitalization(True)
        font.setPointSize(13)
    
        self.input = QLineEdit(self)
        self.input.setFixedWidth(300)
        self.input.setFixedHeight(40)
        self.input.move(140, 100)
        self.input.setStyleSheet("background-color: rgb(220,220,220); color: black; border-radius: 10px; border: 2px solid")
        self.input.setFont(font)
        self.input.setPlaceholderText("enter number")
        # self.input.textChanged.connect(self.button_activation)

        self.button = QPushButton(self)
        self.button.setText("save")
        self.button.setFixedHeight(50)
        self.button.setFixedWidth(140)
        self.button.move(220, 150)
        self.button.setFont(font)
        self.button.setStyleSheet("background-color:  rgb(50,205,50); color: black; border-radius: 10px; border: 2px solid")
        self.button.clicked.connect(self.button_activation)
 
    def button_activation(self):
            input2 = self.input.text()
            changes.changes.Allchanges.barcode_save(self, input2)
            

def main():
    app = QApplication(sys.argv)
    app1 = show_Dataset22()
    app1.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
        