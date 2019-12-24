__author__  = 'Mohammed Shokr <mohammedshokr2014@gmail.com>'
__version__ = 'v 0.1'

"""
JARVIS:
- Control windows programs with your voice
"""

# import modules
from datetime import datetime          # datetime module supplies classes for manipulating dates and times
import subprocess                      # subprocess module allows you to spawn new processes

import speech_recognition as sr        # speech_recognition Library for performing speech recognition with support for Google Speech Recognition, etc..


# Run Application with Voice Command Function
def get_app(Q: str):

    if Q is not None:
        Q = Q.lower()

        if Q == 'hello':
            print('Hi!!')
        elif Q == 'bye' or Q == 'tchau':
            return -1
        elif Q == "time":
            print(datetime.now())
        elif Q == "notepad":
            subprocess.call(['Notepad.exe'])
        elif Q == "calculator":
            subprocess.call(['calc.exe'])
        elif Q == "stikynot":
            subprocess.call(['StikyNot.exe'])
        elif Q == "shell":
            subprocess.call(['powershell.exe'])
        elif Q == "paint":
            subprocess.call(['mspaint.exe'])
        elif Q == "cmd":
            subprocess.call(['cmd.exe'])
        elif Q == "browser":
            subprocess.call(['C:\Program Files\Internet Explorer\iexplore.exe'])
        else:
            print("Sorry ! Try Again")


def listen(r):
    # obtain audios from the microphone

    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        return audio

def recognizar(r, audio):
    # recognize speech using Google Speech Recognition
    try:
        return r.recognize_google(audio)
    except:
        print('problema na recognize.')


while 1:

    r = sr.Microphone()