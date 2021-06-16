
import keyboard
from typing import List, Callable



class TextTracker:

    key_event_tracked: list


    def __init__(self):
        self.key_event_tracked = []
        #self._key_func = lambda self, keyEvent: self.key_event_tracked.append(keyEvent)

    def start_listening_keyboard(self):
        #keyboard.on_release(lambda k:self.text_tracked.append(k))
        # Record events until 'esc' is pressed.
        self.key_event_tracked = keyboard.record(until='esc')

    # def stop_listening_keyboard(self):
    #     keyboard.unhook_all()

    def get_tracked_key_events(self) -> List[keyboard.KeyboardEvent]:
        return self.key_event_tracked