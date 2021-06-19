
import pandas as pd
from streamlit_lib.app_settings import AppSettings
from keyboard import KeyboardEvent
from typing import List, Tuple
import platform

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
        tracked_string = self._try_get_strings(key_events_tracked, allow_backspace=True, event_type='up')
        string_tracked_df = pd.DataFrame({KEY_PARSED_STRING: tracked_string })
        return string_tracked_df

    def get_empty_string_tracked_df(self) -> pd.DataFrame:
        return pd.DataFrame({
            KEY_PARSED_STRING: []
        })


    def get_empty_keyboard_events_tracked_df(self) -> pd.DataFrame:
        return pd.DataFrame({
            KEY_NAME_COLUMN: [],
            KEY_CODE_COLUMN: [],
            KEY_TIME_COLUMN: []
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

    def _try_get_strings(self, events: List[KeyboardEvent], allow_backspace=True, event_type = 'up') -> List[str]:
        """
        Given a sequence of events, tries to deduce what strings were typed.
        Strings are separated when a non-textual key is pressed (such as tab or
        enter). Characters are converted to uppercase according to shift and
        capslock status. If `allow_backspace` is True, backspaces remove the last
        character typed.
    
        This function is a generator, so you can pass an infinite stream of events
        and convert them to strings in real time.

        Note this functions is merely an heuristic. Windows for example keeps per-
        process keyboard state such as keyboard layout, and this information is not
        available for our hooks.

        get_type_strings(event_list, allow_backspace=True,False, event_type='up','down') #-> ['This is what', 'I recorded', '']
        """

        _return_words: List[str] = []
        
        backspace_name = 'delete' if platform.system() == 'Darwin' else 'backspace'

        shift_pressed = False
        capslock_pressed = False
        string = ''
        for event in events:
            name = event.name

            # Space is the only key that we _parse_hotkey to the spelled out name
            # because of legibility. Now we have to undo that.
            if event.name == 'space':
                name = ' '

            if 'shift' in event.name:
                shift_pressed = event.event_type == event_type
            elif event.name == 'caps lock' and event.event_type == event_type:
                capslock_pressed = not capslock_pressed
            elif allow_backspace and event.name == backspace_name and event.event_type == event_type:
                string = string[:-1]
            elif event.event_type == event_type:
                if len(name) == 1:
                    if shift_pressed ^ capslock_pressed:
                        name = name.upper()
                    string = string + name
                else:
                    _return_words.append(string)
                    string = ''
        _return_words.append(string)
        return _return_words