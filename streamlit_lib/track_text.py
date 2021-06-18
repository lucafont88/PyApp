
from queue import Queue
import keyboard
import pandas as pd
import pathlib


class TextTracker:

    # Potrebbe essere inutile   
    def logFocusTime(data_storage, start, end):
        if not pathlib.Path(data_storage).is_file():
            with open(data_storage, "w+") as focus:
                focus.write(f"{start} {end}")
                focus.write("\n")
        else:    
            with open(data_storage, "a") as focus:
                focus.write(f"{start} {end}")
                focus.write("\n")

    _key_event_tracked = []
    def start_listening_keyboard(data_storage = "./focus.txt"):
        # Record events until 'esc' is pressed.
        keyboard.on_release(lambda k: TextTracker._key_event_tracked.append(k))
        # keyboard.start_recording()

    def load_keyboard_events_tracked_df(data_storage = "./focus.txt"):
        path = pathlib.Path(data_storage)
        if path.exists() and path.is_file():
            return pd.read_csv(data_storage) 
    
    def get_empty_keyboard_events_tracked_df():
                return pd.DataFrame({
            'key_names': [],
            'key_codes': [],
            'key_time': []
        })

    def stop_listening_keyboard(data_storage = "./focus.txt"):
        # keyboard.send(hotkey='esc')
        keyboard.unhook_all()
        key_event_tracked_df = TextTracker._get_tracked_key_events_df(TextTracker._key_event_tracked)
        key_event_tracked_df.to_csv(data_storage)

    # def stop_listening_keyboard():
    #     keyboard.unhook_all()


    def _get_tracked_key_events_df(key_event_tracked) -> pd.DataFrame:
        _tracked_keys_names = list(map(lambda k: k.name, key_event_tracked))
        _tracked_keys_codes = list(map(lambda k: k.scan_code, key_event_tracked))
        _tracked_keys_times = list(map(lambda k: k.time, key_event_tracked))

        return pd.DataFrame({
            'key_names': _tracked_keys_names,
            'key_codes': _tracked_keys_codes,
            'key_time': _tracked_keys_times
        })