
import keyboard
from typing import List

class TextTracker:

    text_tracked: List[str]

    def __init__(self):
        self.text_tracked = []

    def start_listening_keyboard(self):
        keyboard.on_release(lambda k:self.text_tracked.append(k))

    def stop_listening_keyboard(self):
        keyboard.on_release(lambda k:self.text_tracked.append(k))