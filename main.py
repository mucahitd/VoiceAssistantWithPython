import speech_recognition as sr
import time
from commands import Command


r = sr.Recognizer()


while True:
    with sr.Microphone() as source:
        print("You can talk master!")
        audio = r.listen(source)


    data = ""
    try:
        data = r.recognize_google(audio, language='tr-tr')
        print(data)
        command = Command(data)
        command.findCommand()
        time.sleep(1)

    except sr.UnknownValueError:
        print("I did not understand!")
