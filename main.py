import sys
import os
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import (
    QApplication, QDialog, QFileDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi
import pyperclip
from transcribe import Transcribe
from Downloader import download

class TranscribeThread(QThread):
    progress_update = pyqtSignal(int)
    finished = pyqtSignal(str)

    def __init__(self, file , txt , Youtube):
        super().__init__()
        self.file = file
        self.txt = txt
        self.Youtube = Youtube

    def run(self):
        self.url = self.txt
        if self.Youtube:
            self.file = download(self.url)
        result = Transcribe(self.file)
        self.finished.emit(result)

class GUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("GUI.ui", self)
        
        self.file_name = ""
        self.outputText.setReadOnly(True)
        self.progressBar.setVisible(False)
        
        self.convertButton.clicked.connect(self.start_transcription)
        self.copyButton.clicked.connect(self.copy_to_clipboard)
        self.saveButton.clicked.connect(self.save_to_file)
        
        self.FileRadio.toggled.connect(self.update_ui)
        self.YoutubeRadio.toggled.connect(self.update_ui)

    def update_ui(self):
        self.inputField.clear()
        if self.FileRadio.isChecked():
            self.open_file_dialog()
            self.inputField.setReadOnly(True)
        elif self.YoutubeRadio.isChecked():
            self.inputField.setReadOnly(False)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_filter = "Audio Files (*.mp3 *.wav)"
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            'Open File',
            '',
            file_filter,
            options=options
        )
        self.inputField.setText(file_name)
        self.file_name = file_name

    def start_transcription(self):
        
        
        if not self.file_name and not self.YoutubeRadio.isChecked():
            QMessageBox.critical(
            self,
            "Error",
            "Please select a file or provide a URL."
            )
            return

        self.progressBar.setVisible(True)
        self.convertButton.setEnabled(False)

        self.transcribe_thread = TranscribeThread(self.file_name,self.inputField.text(),self.YoutubeRadio.isChecked())
        self.transcribe_thread.finished.connect(self.on_transcription_finished)
        self.transcribe_thread.start()

    def on_transcription_finished(self, result):
        if result == "":
            QMessageBox.critical(
            self,
            "Error",
            "An issue occurred most likely because you exceeded the 5-hour monthly limit."
            )
            return
        self.outputText.setPlainText(result)
        self.progressBar.setVisible(False)
        self.convertButton.setEnabled(True)

    def copy_to_clipboard(self):
        result = self.outputText.toPlainText()
        pyperclip.copy(result)

    def save_to_file(self):
        result = self.outputText.toPlainText()
        selected_directory = QFileDialog.getExistingDirectory(
            self, "Select a directory", ""
        )
        if selected_directory:
            file_path = os.path.join(selected_directory, "result.txt")
            with open(file_path, "w") as file:
                file.write(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    window.setWindowTitle("Auto Speech To Text")
    window.show()
    sys.exit(app.exec_())
import sys
import os
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import (
    QApplication, QDialog, QFileDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi
import pyperclip
from transcribe import Transcribe
from Downloader import download

class TranscribeThread(QThread):
    progress_update = pyqtSignal(int)
    finished = pyqtSignal(str)

    def __init__(self, file , txt , Youtube):
        super().__init__()
        self.file = file
        self.txt = txt
        self.Youtube = Youtube

    def run(self):
        self.url = self.txt
        if self.Youtube:
            self.file = download(self.url)
        result = Transcribe(self.file)
        self.finished.emit(result)

class GUI(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("GUI.ui", self)
        
        self.file_name = ""
        self.outputText.setReadOnly(True)
        self.progressBar.setVisible(False)
        
        self.convertButton.clicked.connect(self.start_transcription)
        self.copyButton.clicked.connect(self.copy_to_clipboard)
        self.saveButton.clicked.connect(self.save_to_file)
        
        self.FileRadio.toggled.connect(self.update_ui)
        self.YoutubeRadio.toggled.connect(self.update_ui)

    def update_ui(self):
        self.inputField.clear()
        if self.FileRadio.isChecked():
            self.open_file_dialog()
            self.inputField.setReadOnly(True)
        elif self.YoutubeRadio.isChecked():
            self.inputField.setReadOnly(False)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_filter = "Audio Files (*.mp3 *.wav)"
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            'Open File',
            '',
            file_filter,
            options=options
        )
        self.inputField.setText(file_name)
        self.file_name = file_name

    def start_transcription(self):
        
        
        if not self.file_name and not self.YoutubeRadio.isChecked():
            QMessageBox.critical(
            self,
            "Error",
            "Please select a file or provide a URL."
            )
            return

        self.progressBar.setVisible(True)
        self.convertButton.setEnabled(False)

        self.transcribe_thread = TranscribeThread(self.file_name,self.inputField.text(),self.YoutubeRadio.isChecked())
        self.transcribe_thread.finished.connect(self.on_transcription_finished)
        self.transcribe_thread.start()

    def on_transcription_finished(self, result):
        if result == "":
            QMessageBox.critical(
            self,
            "Error",
            "An issue occurred most likely because you exceeded the 5-hour monthly limit."
            )
            return
        self.outputText.setPlainText(result)
        self.progressBar.setVisible(False)
        self.convertButton.setEnabled(True)

    def copy_to_clipboard(self):
        result = self.outputText.toPlainText()
        pyperclip.copy(result)

    def save_to_file(self):
        result = self.outputText.toPlainText()
        selected_directory = QFileDialog.getExistingDirectory(
            self, "Select a directory", ""
        )
        if selected_directory:
            file_path = os.path.join(selected_directory, "result.txt")
            with open(file_path, "w") as file:
                file.write(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUI()
    window.setWindowTitle("Auto Speech To Text")
    window.show()
    sys.exit(app.exec_())
