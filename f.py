from PyQt5.QtWidgets import QFileDialog

def report(self):
    try:
        # Get the save file path using a file dialog
        save_path, _ = QFileDialog.getSaveFileName(None, "Save Report", "", "Excel Files (*.xlsx)")

        if save_path:
            report = databaseApi2.DatabaseApi("./database/database", "./databaseApi/barcode_images")
            report.report(save_path)  
            QMessageBox.information(None, "Report Saved", "Report has been generated and saved successfully.")
        else:
            QMessageBox.warning(None, "Warning", "No file selected.")
    except Exception as e:
        QMessageBox.warning(None, "Warning", str(e))
