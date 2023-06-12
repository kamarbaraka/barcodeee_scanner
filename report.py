from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import changes.changes
import sys


class Report(QWidget):
    def __init__(self, parent=None):
        super(Report, self).__init__(parent)
        self.resize(500, 600)
        self.setWindowTitle("Report")
        self.setFixedHeight(300)
        self.setFixedWidth(600)
        self.adjustSize()

        # Create a label widget and set its background image
        pixmap = QPixmap('./images/13.png')
        self.background_label = QLabel(self)
        self.background_label.setPixmap(pixmap)
        self.background_label.setGeometry(0, 0, 640, 480)
        self.background_label.setFixedHeight(1000)
        self.background_label.setFixedWidth(1500)

        # Fonts
        font1 = QFont()
        font1.setBold(True)
        font1.setCapitalization(True)
        font1.setPointSize(13)

        font = QFont()
        font.setBold(True)
        font.setCapitalization(True)
        font.setPointSize(9)
        
        self.button = QPushButton(self)
        self.button.setText("Download Report")
        self.button.move(190, 100)
        self.button.setFont(font1)
        self.button.setFixedHeight(50)
        self.button.setFixedWidth(200)
        self.button.setStyleSheet("background-color: rgb(220,220,220); color: rgb(139,0,139); border-radius: 10px")
        self.button.clicked.connect(self.generate_report)

    def generate_report(self):
        changes.changes.Allchanges.report(self)
        
def main():
    app= QApplication(sys.argv)
 
    app1 = Report()
    app1.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
   main()
