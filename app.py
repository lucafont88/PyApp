import streamlit as st
from datetime import datetime
import pandas as pd
from streamlit_lib.track_text import TextTracker
from streamlit_lib.app_settings import AppSettings
import time
import keyboard

TRACKING_FILE_NAME = "./focus.txt"

app_settings = AppSettings(TRACKING_FILE_NAME)
TextTracker.set_app_settings(app_settings)

st.title("Text Tracker")

tracked_data_df: pd.DataFrame = {}

_signal_stop = st.button("Stop")
_signal_start = st.button("Start")

st.write("Results:")

if _signal_start == True:
    TextTracker.start_listening_keyboard()

if _signal_stop == True:
    TextTracker.stop_listening_keyboard()

try:
    tracked_data_df = TextTracker.load_keyboard_events_tracked_df()
except:
    tracked_data_df = TextTracker.get_empty_keyboard_events_tracked_df()

st.write(tracked_data_df)


# keyboard.wait('esc')






# fig = focus_tracker.plotFocus(df_focus)

# st.write(fig)




# # Creating the Dashboard app #
# st.title("Focus Tracker")

# focus_tracker = FocusTracker()

# df_focus, today = focus_tracker.create_focus_df()

# fig = focus_tracker.plotFocus(df_focus)

# st.write(fig)



# # Creating the Dashboard app #
# st.title("Test loop")

# counter = 0

# while True:
#     counter = counter + 1
#     st.write("<h1>" + str(counter) + "</h1>", unsafe_allow_html=True)
#     time.sleep(2.0)
