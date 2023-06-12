import databaseApi.databaseApi2 as databaseApi2, generate.BarcodeGenerator
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Allchanges:
    var = databaseApi2.DatabaseApi("./database/database", "./databaseApi/barcode_images")
    var2 =  generate.BarcodeGenerator.BarcodeGenerator()
    
    def __init__(self, barc_input1, barc_input2):
        self.barc_input1 = barc_input1 
        self.barc_input2 = barc_input2
        
    def barcode_save(self, barc_input1 ):
        # var1 = var2.generate(input1)
        try:
            var1 = Allchanges.var2.generate(int(barc_input1))
            for i in var1:
                Allchanges.var.parse(str(i))
            Allchanges.var.database.close()
            message = QMessageBox()
            message.information(None, "saved", "barcode has been generated and saved successfully")
        except Exception as e:
            message = QMessageBox()
            message.information(None, "not saved", "kindly enter a valid number.")
    
    def kilogram(self,barc_input1, barc_input2):
        try:
            Allchanges.var.set_kg(barc_input1, int(barc_input2))
            QMessageBox.information(None, "saved", "kilograms saved successfully")
        except Exception as e:
            QMessageBox.warning(None, "warning", "Your barcode or weight is invalid. Please try again")
        
    def output(self, barc_input1, label, label1, label2, label3,clear, error, label4,label5, label6):
        
        try:         
            data1 = Allchanges.var
            data2 = data1.fetch(barc_input1)
            # print(data2)
            label1.setText(str(data2[barc_input1]["name"]))
            c= data2[barc_input1]["count"]
            label.setText(str(c ))
            kg = data2[barc_input1]["kg"]
            label2.setText(str(kg))
            
            # total number of plastic saved
            label3.setText(str(c*kg))
            # total_kgs_saved = data2["total_kgs_saved"]
            clear.clear()
            error.clear()
            label4.setText(str(data2["total_kgs_saved"]))
            label5.setText(str(data2["monthly_reuse"]))
            label6.setText(str(data2["total_reuse"]))
            
        except Exception as e:
            error.setText(f"{barc_input1}")
   
        
    def report(self):
        try:
            save_path, _ = QFileDialog.getSaveFileName(None, "Save Report", "", "Excel Files (*.xlsx)")

            if save_path:
                # try:
                progress = QProgressBar()
                progress.setRange(0, 100) 
                # except Exception as e:
                #     QMessageBox.warning(None, "destroyed", "stoped")

                report = Allchanges.var
                def generate_report():
                    r = report.report(save_path)
                    progress.setValue(100)
                    QMessageBox.information(self, "Report Saved", "Report has been generated and saved successfully.")

                thread = QThread()
                thread.started.connect(generate_report)
                thread.start()
            
                # Create a dialog to show the progress bar
                dialog = QDialog(self)
                dialog.setWindowTitle("Downloading")
                layout = QVBoxLayout(dialog)
                layout.addWidget(progress)
                dialog.setModal(True)
                dialog.exec_()
            else:
                QMessageBox.warning(self, "Warning", "No file selected.")
        except Exception as e:
            QMessageBox.warning(self, "Warning", str(e))
        
        
# barc_save = Allchanges(Allchanges.input1, Allchanges.var, Allchanges.var1, Allchanges.var2)    
    
        
        
        
        