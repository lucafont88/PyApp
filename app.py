import streamlit as st
from datetime import datetime
import pandas as pd
from streamlit_lib.track_text import TextTracker
import time
from typing import List
from keyboard import KeyboardEvent

_is_running = False
_any_run = False

st.title("Text Tracker")

text_tracker = TextTracker()
tracked_data_df: pd.DataFrame = {}

if _is_running == True and st.button("Stop"):
    text_tracker.stop_listening_keyboard()
    tracked_data_df = text_tracker.get_tracked_key_events_df()
    _is_running = False

if _is_running == False and st.button("Start"):
    _any_run = True
    _is_running = True
    text_tracker.start_listening_keyboard()
    
if _any_run == True:
    st.write(tracked_data_df)
# else:
#     st.write("No Data")

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
