import streamlit as st
from datetime import datetime
import pandas as pd
from streamlit_lib.track_text import TextTracker
import time
from typing import List
from keyboard import KeyboardEvent

st.title("Text Tracker")

text_tracker = TextTracker()

text_tracker.start_listening_keyboard()

# tracked_keys: List[KeyboardEvent] = text_tracker.get_tracked_key_events()

# tracked_keys_name = map(lambda k: k.name, tracked_keys)

tracked_data_df = text_tracker.get_tracked_key_events_df()

st.write(tracked_data_df)

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
