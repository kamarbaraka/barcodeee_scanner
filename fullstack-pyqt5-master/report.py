from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import databaseApi.databaseApi2 as databaseApi2
import dashboard
import sys 

class report(QWidget):
    def __init__(self , parent=None):
        super(report, self).__init__(parent)
        self.resize(500, 600)
        self.setWindowTitle("report")
        self.setFixedHeight(300)
        self.setFixedWidth(600)
        self.adjustSize()
        # vbox
        
        # Create a label widget and set its background image
        pixmap = QPixmap('./images/13.png')
        self.background_label = QLabel(self)
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, 640, 480)
        self.background_label.setFixedHeight(1000)
        self.background_label.setFixedWidth(1500)
        # fonts
        font1 = QFont()
        font1.setBold(True)
        font1.setCapitalization(True)
        font1.setPointSize(13)

        font = QFont()
        font.setBold(True)
        font.setCapitalization(True)
        font.setPointSize(9)
        # header
        # header
        # self.label = QLabel(self)
        # self.label.setText("REPORTS")
        # self.label.move(150,40)
        # self.label.setFont(font1)
        # self.label.setFixedHeight(30)
        # self.label.setFixedWidth(170)
        # self.label.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")

        self.label = QPushButton(self)
        self.label.setText("download report")
        self.label.move(150,100)
        self.label.setFont(font1)
        self.label.setFixedHeight(50)
        self.label.setFixedWidth(200)
        self.label.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139); border-radius: 10px")
        self.label.clicked.connect(self.report)
        
        dialog = QFileDialog(self)
        dialog.getSaveFileName

    # def save(self):
    #     file_name = QFileDialog.getSaveFileName(None, 'Save File', '', 'Text Files (*)')[0]
    #     if file_name:
    #         with open(file_name, 'w') as f:
    #             f.write('Hello Wpjo9jhdihfidoifhdihfidhifjdojhfidjhfihdihfihfidhidjdjdijiorld!')


    def report(self):
        try:
            file = "./report/report.xlsx"
            report = databaseApi2.DatabaseApi("./database/database", "./databaseApi/barcode_images")
            report.report(file)  
            QMessageBox.information(None, "report saved", "Report has been generated and saved successfully")
        except Exception as e:
            QMessageBox.warning(None, "warning", str(e))  
  
def main():
    
    app = QApplication(sys.argv)
    app1 = report()
    app1.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
        