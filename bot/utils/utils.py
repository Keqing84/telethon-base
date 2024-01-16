import os
import importlib
from pathlib import Path

from telethon import Button


class BtCrt:
    def __init__(self):
        self.btns = []

    def add_url(self, text, url):
        self.btns.append([Button.url(text, url=url)])

    def add_callback(self, text, call_data):
        self.btns.append([Button.inline(text, data=url)])



def load_plugins():
    plugins_folder = "plugins"

    # Iterate through files in the plugins folder
    for file_path in Path(plugins_folder).glob("*.py"):
        # Get the module name from the file name
        module_name = file_path.stem

        # Import the module dynamically
        module = importlib.import_module(f"{plugins_folder}.{module_name}")
