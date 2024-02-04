# Auto Speech To Text Program

The Auto Speech To Text program is a graphical user interface (GUI) application built using PyQt5 that enables users to transcribe audio files or YouTube videos into text. It uses speech recognition technology to convert spoken words into written text. The program provides the option to transcribe local audio files or download audio from YouTube.
Features

Transcribe local audio files (supported formats: .mp3 and .wav).
Download audio from YouTube and transcribe it.
Copy transcribed text to the clipboard.
Save transcribed text to a text file.

# Prerequisites

Python 3.x
PyQt5
pyperclip
transcribe (This should be your own module or code for performing the transcription)
Downloader (This should be your own module or code for downloading audio from YouTube)

# Installation

Install the required packages:


    pip install PyQt5 pyperclip

Download and install the transcribe module (or use your own implementation).

Download and install the Downloader module (or use your own implementation).

# Usage

Run the program:

bash

    python main.py

The GUI window will appear.

Choose the source of the audio:
    Select the "File" radio button to transcribe a local audio file. Click the "Open File" button to choose the file.
    Select the "YouTube" radio button to transcribe audio from a YouTube video. Enter the URL in the input field.

Click the "Convert" button to start the transcription process. The progress will be shown in the progress bar.

Once the transcription is complete, the transcribed text will be displayed in the output text area.

You can copy the transcribed text to the clipboard using the "Copy" button.

To save the transcribed text to a file, click the "Save" button and choose a directory.

# License

## This project is licensed under the MIT License.
## Acknowledgments

This program was developed using the PyQt5 library.
The speech recognition and transcription are powered by the transcribe module.
The audio downloading functionality is supported by the Downloader module.
