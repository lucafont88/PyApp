from queue import Queue
import keyboard
import pandas as pd
import pathlib

q = Queue()

_events = []

keyboard.on_release(lambda k: _events.append(k))

keyboard.wait('esc')

_tracked_keys_names = list(map(lambda k: k.name, _events))
_tracked_keys_codes = list(map(lambda k: k.scan_code, _events))
_tracked_keys_times = list(map(lambda k: k.time, _events))

print(_tracked_keys_names)
print(_tracked_keys_codes)
print(_tracked_keys_times)