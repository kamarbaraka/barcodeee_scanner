import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QCheckBox
from PyQt6.QtCore import Qt


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.__init()

    def __init(self):
        self.setWindowTitle('check boxes')
        self.setGeometry(600, 300, 400, 200)
        self.setMaximumSize(800, 800)

        self.setUpWindow()

        self.show()

    def setUpWindow(self):
        header_label = QLabel('enter the time period you will be available to bea assigned a shift', self)
        header_label.setWordWrap(True)
        header_label.move(30, 10)

        morning_cb = QCheckBox('Morning [8am - 12noon]', self)
        morning_cb.move(10, 40)
        morning_cb.toggled.connect(self.printCheckbox)

        after_cb = QCheckBox('afternoon [12noon - 7pm]', self)
        after_cb.move(10, 60)
        after_cb.toggled.connect(self.printCheckbox)

        night_cb = QCheckBox('night [7pm - 12am]', self)
        night_cb.move(10, 80)
        night_cb.toggled.connect(self.printCheckbox)

        self.text_disp = QLabel(self)
        self.text_disp.setWordWrap(True)
        self.text_disp.setMinimumSize(200, 20)
        self.text_disp.move(5, 120)

    def printCheckbox(self, checked):
        sender = self.sender()

        if checked:
            msg = f'{sender.text()} selected'
            print(msg)
            self.text_disp.setText(msg)
        else:
            msg = f'{sender.text()} deselected'
            print(msg)
            self.text_disp.setText(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
