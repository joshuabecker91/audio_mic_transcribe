# Notes -------------------------------------------------------------------------
# must install the following:
# pip install speechrecognition
# pip install pyttsx3 --user
# -------------------------------------------------------------------------------
# In terminal run: py audio_mic_transcribe.py 
# If transcribed.txt does not exist it will create the file
# Speak into your mic and it will interpret what you said and print to text file
# Listens for a pause to write a new line
# You can edit the text file manually and save at anytime
# -------------------------------------------------------------------------------

import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()

while True:

    try:

        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            with open('transcribed.txt', 'a') as f:
                f.writelines((text)+'\n')
            print(f"Recognized {text}")

    except speech_recognition.UnknownValueError():

        recognizer = speech_recognition.Recognizer()
        continue
