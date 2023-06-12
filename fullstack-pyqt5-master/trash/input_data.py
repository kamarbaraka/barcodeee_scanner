# import EAN13 from barcode module
from barcode import EAN13
import random
import shelve
import sys
  
# import ImageWriter to generate an image file
from barcode.writer import ImageWriter

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys 

class show_Dataset(QWidget):
    def __init__(self , parent=None):
        super(show_Dataset, self).__init__(parent)
        self.resize(500, 600)
        self.setWindowTitle("barcode")
        self.setFixedHeight(600)
        self.setFixedWidth(600)
        self.adjustSize()
        # fonts
        font = QFont()
        font.setBold(True)
        font.setCapitalization(True)
        font.setPointSize(13)
        # header
        self.label = QLabel(self)
        self.label.setText("Enter BARCODE NUMBER")
        self.label.move(150,40)
        self.label.setFont(font)
        # self.label.setFixedHeight(30)
        # self.label.setFixedWidth(170)
        self.label.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")

        self.input = QLineEdit(self)
        self.input.setFixedWidth(300)
        self.input.setFixedHeight(40)
        self.input.move(140, 100)
        self.input.setStyleSheet("background-color: rgb(220,220,220); color: black; border-radius: 10px; border: 2px solid")
        self.input.setFont(font)

        self.label = QLabel(self)
        self.label.setText("reuse counts: ")
        self.label.move(110,300)
        self.label.setFont(font)
        self.label.setFixedHeight(30)
        self.label.setFixedWidth(170)
        self.label.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")

        self.label1 = QLabel(self)
        self.label1.setText("type of material:")
        self.label1.move(110,350)
        self.label1.setFont(font)
        self.label1.setFixedHeight(30)
        self.label1.setFixedWidth(170)
        self.label1.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")

        self.label = QLabel(self)
        self.label.setText("")
        self.label.move(300,300)
        self.label.setFont(font)
        self.label.setFixedHeight(30)
        self.label.setFixedWidth(170)
        self.label.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")

        self.label1 = QLabel(self)
        self.label1.setText("")
        self.label1.move(300,350)
        self.label1.setFont(font)
        self.label1.setFixedHeight(30)
        self.label1.setFixedWidth(170)
        self.label1.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139)")


        self.button = QPushButton(self)
        self.button.setText("send")
        self.button.setFixedHeight(50)
        self.button.setFixedWidth(140)
        self.button.move(220, 150)
        self.button.setFont(font)
        self.button.setStyleSheet("background-color:  rgb(50,205,50); color: black; border-radius: 10px; border: 2px solid")
        self.button.clicked.connect(self.button_activation)
 

    def button_activation(self):
        input = self.input.text()

        try:
            my_code = EAN13(input, writer=ImageWriter())
            my_code.save(f"barcode_images/{random.randint(10000,20000)}")
            
            
        except Exception as e:
            message = QMessageBox()
            message.information(None, "saved", str(e))
        
    
        class DatabaseApi:

            try:
                database = shelve.open('database')
                #database = {}
            except FileExistsError:
                print("database exists")

            def parse(self, barcode):
                self.database[barcode] = dict(count=0, type_of_material='plastic')
                self.database['sales'] = 0
                self.database.close()

            @staticmethod
            def fetch(barcode):
                database = shelve.open('database', writeback=True)
                #print(database)
                database[str(barcode)]['count'] += 1
                barcode_data = database.get(str(barcode))
                #print(barcode_data)
                return barcode_data


        if __name__ == '__main__':
            db = DatabaseApi()
            # while True:
            inp = input
            # if inp == 'do':
            #     break
            db.parse(str(inp))
            message = QMessageBox()
            message.information(None, "saved", "barcode has been generated successfully")
            # while True:
            #     inpt = input('enter barcodes')
            #     if inpt == 'exit':
            #         break
            #     try:
            #         print(db.fetch(inpt))
            #     except KeyError:
            #         print('scan again')
            #         print()
            #         continue
            sys.exit(25)
        return input


       
  
# Our barcode is ready. Let's save it.
        

        

        
        
def main():
    app = QApplication(sys.argv)
    app1 = show_Dataset()
    app1.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()
        