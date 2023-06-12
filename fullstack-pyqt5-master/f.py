from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QFile
from PyQt5.QtGui import *

def save_file():
    file_name = QFileDialog.getSaveFileName(None, 'Save File', '', 'Text Files (*.txt)')[0]
    if file_name:
        with open(file_name, 'w') as f:
            f.write('Hello World!')

save_file()
