import speech_recognition as sr
import os
from scripts import go_to_page,zoom_out,zoom_in



def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio)

            print("You said: " + command)

            if "go to page" in command:
                page_num = command.split("go to page")[1].strip()
                print(page_num, "page number")
                go_to_page(page_num)

            if "get closer" in command:
                zoom_in()
            if "away" in command:
                zoom_out()

            return command
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                f"Could not request results from Google Speech Recognition service; {e}")


def perform_action(command):
    if command.lower() == 'next page':
        os.system(
            """osascript -e 'tell application "System Events" to tell process "Preview" to key code 124'""")
    elif command.lower() == 'previous page':
        os.system(
            """osascript -e 'tell application "System Events" to tell process "Preview" to key code 123'""")


while True:
    command = listen_for_command()
    if command:
        perform_action(command)