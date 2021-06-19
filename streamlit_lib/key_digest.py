
import pandas as pd
from streamlit_lib.app_settings import AppSettings
from keyboard import KeyboardEvent, get_typed_strings
from typing import List, Tuple

KEY_NAME_COLUMN = 'key_names'
KEY_CODE_COLUMN = 'key_codes'
KEY_TIME_COLUMN = 'key_time'


KEY_PARSED_STRING = 'parsed_string'

class KeyDigest:
    _app_settings: AppSettings

    def __init__(self, app_settings: AppSettings):
        self._app_settings = app_settings

    def digest_session(self, key_events_tracked: List[KeyboardEvent])-> pd.DataFrame:
        tracked_df = self._tracked_list_to_dataframe(key_events_tracked)
        return tracked_df

    def key_event_generator(self, key_events_tracked: List[KeyboardEvent]):
        for k in key_events_tracked:
            yield k

    def euristics_string_parser(self, key_events_tracked: List[KeyboardEvent]) -> pd.DataFrame:
        tracked_string = get_typed_strings(self.key_event_generator(key_events_tracked), allow_backspace=True)
        string_tracked_df = pd.DataFrame({KEY_PARSED_STRING: tracked_string })
        return string_tracked_df

    def get_empty_string_tracked_df(self) -> pd.DataFrame:
            return pd.DataFrame({
        KEY_NAME_COLUMN: [],
        KEY_CODE_COLUMN: [],
        KEY_TIME_COLUMN: []
    })

    def get_empty_keyboard_events_tracked_df(self) -> pd.DataFrame:
                return pd.DataFrame({
            KEY_PARSED_STRING: []
        })

    def _tracked_list_to_dataframe(self, keys_events_list: List[KeyboardEvent]) -> pd.DataFrame:
        _tracked_keys_names = list(map(lambda k: k.name, keys_events_list))
        _tracked_keys_codes = list(map(lambda k: k.scan_code, keys_events_list))
        _tracked_keys_times = list(map(lambda k: k.time, keys_events_list))

        return pd.DataFrame({
            KEY_NAME_COLUMN: _tracked_keys_names,
            KEY_CODE_COLUMN: _tracked_keys_codes,
            KEY_TIME_COLUMN: _tracked_keys_times
        }) 
