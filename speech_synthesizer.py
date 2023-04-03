# NAME: Maalug Mary Yabia
# Student ID: 10971409
# Department: Biomedical Engineering

import pyttsx3

# Creating An Organised class for processing the text and speaking it

# Initializing the speech engine
engine = pyttsx3.init()


# This class take 4 arguments which depending on the various arguments will dipict how the program runs
class Synthesizer:
    def __init__(self, text_to_speak, voice_id, volume, speed):
        self.text_to_speak = text_to_speak
        self.voice_id = voice_id
        self.volume = volume
        self.speed = speed
        self.speakText()

    def setVoice(self):
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[self.voice_id].id)

    def setVolume(self):
        engine.setProperty('volume', self.volume)

    def setSpeed(self):
        engine.setProperty('rate', self.speed)

    def speakText(self):
        self.setVoice()
        self.setVolume()
        self.setSpeed()
        engine.say(self.text_to_speak)
        engine.runAndWait()
        engine.stop()
