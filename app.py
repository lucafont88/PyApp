import streamlit as st
from datetime import datetime
import pandas as pd
from streamlit_lib.track_text import TextTracker
import time

# Creating the Dashboard app #
st.title("Text Tracker")

text_tracker = TextTracker()

df_focus, today = focus_tracker.create_focus_df()

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
