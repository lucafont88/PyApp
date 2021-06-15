import streamlit as st
from datetime import datetime
import pandas as pd
from streamlit_lib.track_focus import FocusTracker

# Creating the Dashboard app #
st.title("Focus Tracker")

focus_tracker = FocusTracker()

df_focus, today = focus_tracker.create_focus_df()

fig = focus_tracker.plotFocus(df_focus)

st.write(fig)