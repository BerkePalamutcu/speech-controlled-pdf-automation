
import os
import tempfile
import subprocess

def go_to_page(page_number):
    applescript = f"""
    tell application "Preview"
        activate
        tell application "System Events"
            keystroke "g" using {{command down, option down}} -- Shortcut to go to page
            delay 1 -- Wait for the 'Go to Page' dialog to appear
            keystroke "{page_number}" -- Type the page number
            delay 1 -- Wait for the page number to be entered
            keystroke return -- Press Enter to go to the page
        end tell
    end tell
    """
    with tempfile.NamedTemporaryFile(suffix=".applescript", delete=False) as temp:
        temp.write(applescript.encode())
        temp.close()
        os.system(f"osascript {temp.name}")
        os.remove(temp.name)


def zoom_in():
    applescript = """
    tell application "Preview"
        activate
    end tell
    tell application "System Events"
        tell process "Preview"
            keystroke "+" using command down
        end tell
    end tell
    """
    subprocess.run(['osascript', '-e', applescript])


def zoom_out():
    applescript = """
    tell application "Preview"
        activate
    end tell
    tell application "System Events"
        tell process "Preview"
            keystroke "-" using command down
        end tell
    end tell
    """
    subprocess.run(['osascript', '-e', applescript])
