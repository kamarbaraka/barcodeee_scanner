import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QLineEdit
from PyQt6.QtGui import QFont


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.__init()

    def __init(self):
        self.setWindowTitle('search')
        self.resize(500, 200)

        self.__setUpWindow()

        self.show()

    def __setUpWindow(self):
        header_label = QLabel(
            """<h1>Search Catalogue</h1>""",
            self
        )
        header_label.setFont(QFont('Arial', 10))
        header_label.move(120, 10)

        sub_label = QLabel('enter the name to search in the search box', self)
        sub_label.setFont(QFont('Arial', 15))
        sub_label.move(70, 40)

        name_tag = QLabel('<h3>Name</h3>', self)
        name_tag.setFont(QFont('Arial', 12))
        name_tag.resize(60, 40)
        name_tag.move(5, 70)

        name_edit = QLineEdit(self)
        name_edit.setPlaceholderText('enter name as: First Last')
        name_edit.resize(400, 40)
        name_edit.move(80, 70)
        self.line_edit = name_edit

        search_button = QPushButton('search', self)
        search_button.setFont(QFont('Arial', 12))
        search_button.resize(200, 40)
        search_button.move(150, 120)
        search_button.clicked.connect(self.__search)

    def __search(self):
        file = 'catalogue.txt'

        try:
            with open(file, 'r') as catalogue:
                for line in catalogue:
                    if self.line_edit.text() == line.strip():
                        answer1 = (
                            QMessageBox.information(
                                self,
                                'Author found',
                                f"""<p>Author found</p><p>{line}</p><p>Do you wish to continue?</p>""",
                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                QMessageBox.StandardButton.Yes
                            ))
                        print('take 1')

                        if answer1 == QMessageBox.StandardButton.No:
                            QMessageBox.warning(self, 'closing', 'closing application...')
                            self.close()
                            print('take 2')
                            return 0

                    else:
                        answer1 = QMessageBox.information(
                            self,
                            'auther Not Found',
                            """<p>Author Not Found!</p><p>Continue?</p>""",
                            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                            QMessageBox.StandardButton.Yes
                        )
                        print('take 3')

                        if answer1 == QMessageBox.StandardButton.No:
                            print('take 4')
                            self.close()
                            return 0

        except FileNotFoundError as error:
            answer1 = (
                QMessageBox.information(
                    self,
                    'file not found',
                    f"""<p>File Not Found!</p><p>{error}</p><p>Continue?</p>""",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                    QMessageBox.StandardButton.No
                ))
            if answer1 == QMessageBox.StandardButton.No:
                self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
