from typing import Tuple
import pandas as pd
from datetime import datetime
import numpy as np
import time
import pathlib
import plotly.graph_objs as go


class FocusTracker:

    FOCUS_DATA_PATH: str

    def __init__(self, focus_data_path: str = None):
        if focus_data_path == None:
            self.FOCUS_DATA_PATH = "./focus.txt"
        else:
            self.FOCUS_DATA_PATH = focus_data_path

    
    def create_focus_df(self) -> Tuple[pd.DataFrame, str]:
        today = datetime.strftime(datetime.today(),format="%Y-%m-%d")
        timeStartsStamp,dateStartsStamp,durations= self._loadFocus()
        df = pd.DataFrame(dict(dates=dateStartsStamp, focus=durations))
        return df, today

    def plotFocus(self, df: pd.DataFrame):
        # df = pd.DataFrame(df)
        df_focus_daily = pd.DataFrame(df.groupby(["dates"]).sum())
        mean_focus_time = round(df_focus_daily["focus"].mean(),2)
        focusBar = go.Bar(x=df_focus_daily.index,y=df_focus_daily["focus"],
                        name="Focus",marker_color="green")
        focusTrend = go.Scatter(x=df_focus_daily.index,y=df_focus_daily["focus"],    
                        name="Focus",marker_color="red")
        fig = go.Figure(data=[focusTrend,focusBar])
        fig.update_layout(title=f"Overview, Average Focus Time: {mean_focus_time} hours")
        fig.update_yaxes(title="Focus (h)")
        # fig.show()
        return fig

    def _logFocusTime(self, start, end):
        if not pathlib.Path(self.FOCUS_DATA_PATH).is_file():
            with open(self.FOCUS_DATA_PATH, "w+") as focus:
                focus.write(f"{start} {end}")
                focus.write("\n")
        else:    
            with open(self.FOCUS_DATA_PATH, "a") as focus:
                focus.write(f"{start} {end}")
                focus.write("\n")


    def _trackFocus(self):
        start = int(time.time())
        end_session = input("Press to finish tracking")
        end = int(time.time())
        total = (end - start) / 3600
        print(f"Tracked: {total} hours")

        today_total = self.calculateFocusTime()

        print(f"Total focus time tracked today: {today_total}")

        self._logFocusTime(start, end)


    def _loadFocus(self):
        with open(self.FOCUS_DATA_PATH, "r") as focus:
            focusData = [f.strip("\n") for f in focus.readlines()]

        timeStarts = np.array([int(f.split()[0]) for f in focusData])
        timeEnds = np.array([int(f.split()[1]) for f in focusData])

        durations = (timeEnds - timeStarts)/3600
        timeStartsStamp = [datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')\
                           for ts in timeStarts]
        dateStartsStamp = [datetime.fromtimestamp(ts).strftime('%Y-%m-%d')\
                           for ts in timeStarts]
        
        return timeStartsStamp,dateStartsStamp,durations

    def _calculateFocusTime(self):
        df, today = self.create_focus_df()
        todayFocus = df[df["dates"] == today].sum()

        return todayFocus

if __name__=="__main__":
    # logFocusTime()
    main_focus_tracker = FocusTracker()
    main_focus_tracker._trackFocus