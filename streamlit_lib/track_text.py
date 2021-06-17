
import keyboard
from typing import List
import pandas as pd



class TextTracker:

    key_event_tracked: list


    def __init__(self):
        self.key_event_tracked = []
        #self._key_func = lambda self, keyEvent: self.key_event_tracked.append(keyEvent)

    def start_listening_keyboard(self):
        #keyboard.on_release(lambda k:self.text_tracked.append(k))
        # Record events until 'esc' is pressed.
        self.key_event_tracked = keyboard.record(until='esc')

    def stop_listening_keyboard(self):
        keyboard.send(hotkey='esc')
    # def stop_listening_keyboard(self):
    #     keyboard.unhook_all()

    def get_raw_tracked_key_events(self) -> List[keyboard.KeyboardEvent]:
        return self.key_event_tracked

    def get_tracked_key_events_df(self) -> pd.DataFrame:
        _tracked_keys_names = list(map(lambda k: k.name, self.key_event_tracked))
        _tracked_keys_codes = list(map(lambda k: k.scan_code, self.key_event_tracked))
        _tracked_keys_times = list(map(lambda k: k.time, self.key_event_tracked))

        return pd.DataFrame({
            'key_names': _tracked_keys_names,
            'key_codes': _tracked_keys_codes,
            'key_time': _tracked_keys_times
        })