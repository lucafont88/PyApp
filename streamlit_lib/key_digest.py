
import pandas as pd
from streamlit_lib.app_settings import AppSettings


class KeyDigest:
    _app_settings: AppSettings

    def __init__(self, app_settings: AppSettings):
        self._app_settings = app_settings

    def digest_session(self, key_events_tracked: list)-> pd.DataFrame:
        tracked_df = self._tracked_list_to_dataframe(key_events_tracked)
        return tracked_df

    def _tracked_list_to_dataframe(self, keys_events_list: list) -> pd.DataFrame:
        _tracked_keys_names = list(map(lambda k: k.name, keys_events_list))
        _tracked_keys_codes = list(map(lambda k: k.scan_code, keys_events_list))
        _tracked_keys_times = list(map(lambda k: k.time, keys_events_list))

        return pd.DataFrame({
            'key_names': _tracked_keys_names,
            'key_codes': _tracked_keys_codes,
            'key_time': _tracked_keys_times
        })
