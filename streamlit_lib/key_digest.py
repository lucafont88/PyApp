
from streamlit_lib.app_settings import AppSettings


class KeyDigest:
    _app_settings: AppSettings

    def __init__(self, app_settings):
        self._app_settings = app_settings