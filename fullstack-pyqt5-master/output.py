from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import databaseApi.databaseApi2 as databaseApi2
import sys , random

class show_Dataset(QWidget):
    def __init__(self , parent=None):
        super(show_Dataset, self).__init__(parent)
        self.resize(500, 600)
        self.setWindowTitle("Retrieve Data")
        self.setFixedHeight(600)
        self.setFixedWidth(1200)
        self.adjustSize()
        self.setStyleSheet("color: black")
        self.setWindowIcon(QIcon('./images/logo.png'))

        # Create a label widget and set its background image
        pixmap = QPixmap('./images/13.png')
        self.background_label = QLabel(self)
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, 640, 480)
        self.background_label.setFixedHeight(1000)
        self.background_label.setFixedWidth(1500)

        # self.background_label.move(600, 10)
        # self.setStyleSheet("background-image: url(12.png);")

        # vbox
        
        # fonts
        font = QFont()
        font.setBold(True)
        font.setCapitalization(True)
        font.setPointSize(13)
    

        self.input = QLineEdit(self)
        self.input.setFixedWidth(400)
        self.input.setFixedHeight(40)
        self.input.move(100, 100)
        self.input.setStyleSheet("background-color: rgb(220,220,220); color: black; border-radius: 10px; border: 2px solid")
        self.input.setFont(font)
        self.input.setPlaceholderText("Scan or enter the container code")
        self.input.textChanged.connect(self.output)
        

        self.label = QLabel(self)
        self.label.setText("reuse counts: ")
        self.label.move(110,350)
        self.label.setFont(font)
        self.label.setFixedHeight(30)
        self.label.setFixedWidth(180)
        self.label.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")

        self.label1 = QLabel(self)
        self.label1.setText("refill Container:")
        self.label1.move(110,300)
        self.label1.setFont(font)
        self.label1.setFixedHeight(30)
        self.label1.setFixedWidth(180)
        self.label1.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")

        self.label2 = QLabel(self)
        self.label2.setText("Kilograms:")
        self.label2.move(110,400)
        self.label2.setFont(font)
        self.label2.setFixedHeight(30)
        self.label2.setFixedWidth(180)
        self.label2.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")

        self.label2 = QLabel(self)
        self.label2.setText("weight saved")
        self.label2.move(110,450)
        self.label2.setFont(font)
        self.label2.setFixedHeight(30)
        self.label2.setFixedWidth(180)
        self.label2.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")

        self.label2 = QLabel(self)
        self.label2.setText("total weight saved")
        self.label2.move(550,300)
        self.label2.setFont(font)
        self.label2.setFixedHeight(30)
        self.label2.setFixedWidth(180)
        self.label2.setStyleSheet("background-color: rgb(128,128,128); color: black;")

        self.label2 = QLabel(self)
        self.label2.setText("monthly reuse")
        self.label2.move(550,350)
        self.label2.setFont(font)
        self.label2.setFixedHeight(30)
        self.label2.setFixedWidth(180)
        self.label2.setStyleSheet("background-color: rgb(128,128,128); color: black;")

        self.label2 = QLabel(self)
        self.label2.setText("total count")
        self.label2.move(550,400)
        self.label2.setFont(font)
        self.label2.setFixedHeight(30)
        self.label2.setFixedWidth(180)
        self.label2.setStyleSheet("background-color: rgb(128,128,128); color: black;")

        # count
        self.label = QLabel(self)
        self.label.move(300,350)
        self.label.setFont(font)
        self.label.setFixedHeight(30)
        self.label.setFixedWidth(170)
        self.label.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")

        # reuse
        self.label1 = QLabel(self)
        self.label1.move(300,300)
        self.label1.setFont(font)
        self.label1.setFixedHeight(30)
        self.label1.setFixedWidth(170)
        self.label1.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")

        # kilograms
        self.label2 = QLabel(self)
        self.label2.move(300,400)
        self.label2.setFont(font)
        self.label2.setFixedHeight(30)
        self.label2.setFixedWidth(170)
        self.label2.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")

        # amount of plastic saved
        self.label3 = QLabel(self)
        self.label3.move(300,450)
        self.label3.setFont(font)
        self.label3.setFixedHeight(30)
        self.label3.setFixedWidth(170)
        self.label3.setStyleSheet("background-color: rgb(220,220,220); color: green;")

         # total amount of plastic saved
        self.label4 = QLabel(self)
        self.label4.move(750,300)
        self.label4.setFont(font)
        self.label4.setFixedHeight(30)
        self.label4.setFixedWidth(80)
        self.label4.setStyleSheet("background-color: black; color: white")

        # total counts
        self.label5 = QLabel(self)
        self.label5.move(750,350)
        self.label5.setFont(font)
        self.label5.setFixedHeight(30)
        self.label5.setFixedWidth(80)
        self.label5.setStyleSheet("background-color: black; color: white")

        # total counts
        self.label6 = QLabel(self)
        self.label6.move(750,400)
        self.label6.setFont(font)
        self.label6.setFixedHeight(30)
        self.label6.setFixedWidth(80)
        self.label6.setStyleSheet("background-color: black; color: white")
        
        # error messages
        self.error = QLabel(self)
        self.error.move(110,200)
        self.error.setFont(font)
        self.error.setFixedHeight(30)
        self.error.setFixedWidth(400)
        self.error.setStyleSheet("background-color: rgb(0,191,255) ; color: red;")

        # self.button = QPushButton(self)
        # self.button.setText("download")
        # self.button.setFixedHeight(50)
        # self.button.setFixedWidth(140)
        # self.button.move(350, 500)
        # self.button.setFont(font)
        # self.button.setStyleSheet("background-color:  rgb(50,205,50); color: black; border-radius: 10px; border: 2px solid")
        # self.button.clicked.connect(self.output)

    def output(self):
        try:         
            input = self.input.text()
            data1 = databaseApi2.DatabaseApi("./database/database", "./databaseApi/barcode_images")
            data2 = data1.fetch(input)
            print(data2)
            self.label1.setText(str(data2[input]["name"]))
            c= data2[input]["count"]
            self.label.setText(str(c ))
            kg = data2[input]["kg"]
            self.label2.setText(str(kg))
            
            # total number of plastic saved
            self.label3.setText(str(c*kg))
            total_kgs_saved = [0]
            total_kgs_saved[0] = data2["total_kgs_saved"]
            self.error.clear()
            self.input.clear()
            self.label4.setText(str(total_kgs_saved[0]))
            self.label5.setText(str(data2["monthly_reuse"]))
            self.label6.setText(str(data2["total_reuse"]))
            
        except Exception as e:
            self.error.setText(f"{input}")
   
def main():
    
    app = QApplication(sys.argv)
    app1 = show_Dataset()
    app1.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
        