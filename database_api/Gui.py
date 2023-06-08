from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys 


class ShowDataset(QWidget):
    count = 0

    def __init__(self, parent=None):
        super(ShowDataset, self).__init__(parent)
        self.resize(500, 600)
        self.setWindowTitle("barcode")
        self.setFixedHeight(600)
        self.setFixedWidth(600)
        self.adjustSize()

        counter_display = QLabel(self)
        counter_display.setText(str(self.count))

    def output(self, count):
        self.count = count

    def init(self):
        app = QApplication(sys.argv)
        app1 = ShowDataset()
        app1.show()
        sys.exit(app.exec())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app1 = ShowDataset()
    app1.show()
    sys.exit(app.exec())
        