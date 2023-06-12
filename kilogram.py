from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import changes.changes
import sys 

class kilogram(QWidget):
    def __init__(self , parent=None):
        super(kilogram, self).__init__(parent)
        self.resize(500, 600)
        self.setWindowTitle("weight")
        self.setFixedHeight(600)
        self.setFixedWidth(600)
        self.adjustSize()
        self.setWindowIcon(QIcon('./images/logo.png'))
        # self.setStyleSheet("background-image: url(./images/12.png);")
        # Create a label widget and set its background image
        pixmap = QPixmap('./images/13.png')
        self.background_label = QLabel(self)
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, 640, 480)
        self.background_label.setFixedHeight(1000)
        self.background_label.setFixedWidth(1500)
        # vbox
        
        # fonts
        font = QFont()
        font.setBold(True)
        font.setCapitalization(True)
        font.setPointSize(13)
        # header
        # self.label = QLabel(self)
        # self.label.setText("add weight")
        # self.label.move(170,40)
        # self.label.setFont(font)
        # # self.label.setFixedHeight(30)
        # # self.label.setFixedWidth(170)
        # self.label.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")

        self.input = QLineEdit(self)
        self.input.setFixedWidth(400)
        self.input.setFixedHeight(40)
        self.input.move(150, 150)
        self.input.setStyleSheet("background-color: rgb(220,220,220); color: black; border-radius: 10px; border: 2px solid")
        self.input.setFont(font)
        self.input.setPlaceholderText("Scan or enter barcode")

        self.label = QLabel(self)
        self.label.setText("barcode ")
        self.label.move(18,155)
        self.label.setFont(font)
        self.label.setFixedHeight(30)
        self.label.setFixedWidth(180)

        self.input2 = QLineEdit(self)
        self.input2.setFixedWidth(400)
        self.input2.setFixedHeight(40)
        self.input2.move(150, 230)
        self.input2.setStyleSheet("background-color: rgb(220,220,220); color: black; border-radius: 10px; border: 2px solid")
        self.input2.setFont(font)
        self.input2.setPlaceholderText("Enter number of kgs")

        self.label1 = QLabel(self)
        self.label1.setText("weight (kgs) ")
        self.label1.move(18,235)
        self.label1.setFont(font)
        self.label1.setFixedHeight(30)
        self.label1.setFixedWidth(180)

        self.button = QPushButton(self)
        self.button.setText("save")
        self.button.setFixedHeight(50)
        self.button.setFixedWidth(140)
        self.button.move(220, 300)
        self.button.setFont(font)
        self.button.setStyleSheet("background-color:  rgb(50,205,50); color: black; border-radius: 10px; border: 2px solid")
        self.button.clicked.connect(self.output)

    def output(self):
        barcode = self.input.text()
        kgs = self.input2.text()
        changes.changes.Allchanges.kilogram(self, barcode, kgs)
    
def main():
    
    app = QApplication(sys.argv)
    app1 = kilogram()
    app1.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
        