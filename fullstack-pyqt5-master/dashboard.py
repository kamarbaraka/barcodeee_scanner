from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys, os

import databaseApi.databaseApi2
import output, barcode_save as barcode_save, kilogram, report 

class dashboard(QWidget):
    def __init__(self , parent=None):
        super(dashboard, self).__init__(parent)
        
        pixmap = QPixmap('./images/13.png')

        # Create a label widget and set its background image
        self.background_label = QLabel(self)
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, 640, 480)
        self.background_label.setFixedHeight(720)
        self.background_label.setFixedWidth(1366)
        self.setStyleSheet("background-image: url(./images/3 (1).jpeg);")
        self.resize(500, 600)
        self.setWindowTitle("administrative dashboard")
        self.isFullScreen()
        self.adjustSize()
        self.setWindowIcon(QIcon('./images/logo.png'))
        # self.setStyleSheet("background-image: url(12.png);")
        # fonts
        font = QFont()
        font.setBold(True)
        font.setCapitalization(True)
        font.setPointSize(13)
        # header
        self.label = QLabel(self)
        self.label.setText("Welcome to administrative dashboard")
        self.label.move(450,20)
        self.label.setFont(font)
        self.label.setFixedHeight(70)

         # add kilograms
        self.button2 = QPushButton(self)
        self.button2.setFont(font)
        self.button2.setFixedWidth(200)
        self.button2.setFixedHeight(70)
        self.button2.setText("generate barcodes")
        self.button2.move(230, 100)
        self.button2.setStyleSheet("background-color: rgb(100,149,237); border-radius: 10px; color: black")
        self.button2.clicked.connect(self.save_data)
        # button0
        self.button1 = QPushButton(self)
        self.button1.setFont(font)
        self.button1.setFixedWidth(200)
        self.button1.setFixedHeight(70)
        self.button1.setText("add weight")
        self.button1.move(450, 100)
        self.button1.setStyleSheet("background-color: rgb(100,149,237); border-radius: 10px; color: black")
        self.button1.clicked.connect(self.kilograms)

        # Save to database
        self.button2 = QPushButton(self)
        self.button2.setFont(font)
        self.button2.setFixedWidth(200)
        self.button2.setFixedHeight(70)
        self.button2.setText("Retrieve data")
        self.button2.move(670, 100)
        self.button2.setStyleSheet("background-color: rgb(100,149,237); border-radius: 10px; color: black")
        self.button2.clicked.connect(self.retrieve)

        # Save to database
        self.button2 = QPushButton(self)
        self.button2.setFont(font)
        self.button2.setFixedWidth(200)
        self.button2.setFixedHeight(70)
        self.button2.setText("REPORTS")
        self.button2.move(890, 100)
        self.button2.setStyleSheet("background-color: rgb(100,149,237); border-radius: 10px; color: black")
        self.button2.clicked.connect(self.reports)
    
    
    def mainFunction():
        report = databaseApi.databaseApi2.DatabaseApi("./database/database", "./databaseApi/barcode_images") 
        return report

    def retrieve(self):
        self.roles = output.show_Dataset()
        self.roles.show()

    def save_data(self):
        self.addusers = barcode_save.show_Dataset22()
        self.addusers.show()

    def kilograms(self):
        self.addusers = kilogram.kilogram()
        self.addusers.show()
    
    def reports(self):
        # file = "./report/report.xlsx"
        # r = show_Dataset.mainFunction()
        # r.report(file)
        self.addusers = report.report()
        self.addusers.show()
        # QMessageBox.information(None, "report saved", "Report has been generated and saved successfully")



        
def main():
    try:
        os.mkdir('./databaseApi/database')
    except Exception:
        pass
    try:
        os.mkdir('./databaseApi/barcode_images')
    except FileExistsError:
        pass
    app = QApplication(sys.argv)
    app1 = dashboard()
    # app1.setStyleSheet("background-image: url(12.png)")
    app1.showMaximized()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
        