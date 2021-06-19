from streamlit_lib.app_settings import AppSettings
from streamlit_lib.key_digest import KeyDigest
from streamlit_lib.track_text import TextTracker
import keyboard

def key_pressed_generator(key_pressed: list):
    for k in key_pressed:
        print(k)
        yield k

def generate_events():
    while True:
        k = keyboard.read_key()
        print(k)
        yield keyboard.read_key()

key_pressed = []
keyboard.on_release(lambda k: key_pressed.append(k))

print("listening...")

keyboard.wait('esc')
print("stop listening")
print("---- Keys ------")
print(key_pressed)

TRACKING_FILE_NAME = "./focus.txt"
PARSED_STRING_FILE_NAME = "./euristic_string.txt"

app_settings = AppSettings(TRACKING_FILE_NAME, PARSED_STRING_FILE_NAME)

TextTracker.set_app_settings(app_settings)

key_digest = KeyDigest(app_settings)

result = TextTracker.load_parsed_strings_df() # key_digest.try_get_strings(key_pressed)

print("----Parsed strings:----")

print (result)

print("  *-*-*-*-*-*-*-*-*- ")
print("End")