# NAME: Maalug Mary Yabia
# Student ID: 10971409
# Department: Biomedical Engineering

import PySimpleGUI as simpleGui

import speech_synthesizer
from speech_gui import window

voice = 0
volume = 0.5
speed = 200

while True:
    event, values = window.read()
    if event == simpleGui.WINDOW_CLOSED:
        break
    # Checking to see if the volume slider has been moved from its original position
    # Also the volume of the speech engine has a range of 0.1 as lowest to 1 as highest
    # But our slider has a range of 1 to 10, so when we get the current value of the slider
    # we multiply it by 0.1 to get the corresponding value between 0.1 and 1
    if event == '-VOL-':
        volume = values['-VOL-'] * 0.1

    # Checking to see if the Speed slider has been moved from its original position
    # Also the speed of the speech engine known as rate has a range of 50 as lowest to 300 as highest
    # so  we get the current value of the slider and set it to the speed variable
    if event == '-SPEED-':
        speed = values['-SPEED-']

    # After the user clicks the Speak button we check to see which radio button is select and know that by default
    # the male radio button is selected. Then if the user doesn't change the male radio button to female
    # we just pass 0 to the voice variable or the vice versa and pass 1 for female voice to the voice variable
    # Then we call the Speech Synthesizer class which is Synthesizer and pass all the arguments to make the engine
    # perform its job
    if event == 'Speak':
        if values['-MALE-RB-']:
            voice = 0
        elif values['-FEMALE-RB-']:
            voice = 1
        speech_synthesizer.Synthesizer(values['-INPUT-TEXT-'], voice, volume, speed)

window.close()
