
from queue import Queue
from streamlit_lib.key_digest import KeyDigest
from streamlit_lib.app_settings import AppSettings
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

    _app_settings: AppSettings
    def set_app_settings(app_settings: AppSettings) -> None:
        TextTracker._app_settings = app_settings
    
    def _get_app_settings() -> AppSettings:
        if TextTracker._app_settings == None:
            raise Exception("Not defined app setrings")
        return TextTracker._app_settings


    _key_event_tracked = []
    def start_listening_keyboard():
        keyboard.on_release(lambda k: TextTracker._handle_key_event(k))

    def _handle_key_event(key):
        TextTracker._key_event_tracked.append(key)

    def load_keyboard_events_tracked_df():
        data_storage = TextTracker._app_settings.tracking_file_name
        path = pathlib.Path(data_storage)
        if path.exists() and path.is_file():
            return pd.read_csv(data_storage) 
    
    def get_empty_keyboard_events_tracked_df():
                return pd.DataFrame({
            'key_names': [],
            'key_codes': [],
            'key_time': []
        })

    def stop_listening_keyboard():
        app_settings = TextTracker._get_app_settings()
        data_storage = app_settings.tracking_file_name
        keyboard.unhook_all()
        key_digest = KeyDigest(app_settings)
        key_digest.digest_session(TextTracker._key_event_tracked)
        key_event_tracked_df = key_digest.digest_session(TextTracker._key_event_tracked)
        key_event_tracked_df.to_csv(data_storage)