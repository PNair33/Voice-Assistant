import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()


def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises...Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Ask me anything...")
        recordedaudio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google_cloud(recordedaudio, language='en_US')
        command = command.lower()
        print("Your message: ", format(command))
    except Exception as ex:
        print(ex)

    if 'chrome' in command:
        say = "Opening chrome browser..."
        engine.say(say)
        engine.runAndWait()
        program = "/Applications/Google Chrome.app"
        subprocess.Popen([program])

    if 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        print(time)
        engine.say(time)
        engine.runAndWait()

    if 'youtube' in command:
        say = 'opening youtube...'
        engine.say(say)
        engine.runAndWait()
        webbrowser.open('www.youtube.com')

    if 'quit' in command:
        word = False


word = True
while word:
    cmd()

