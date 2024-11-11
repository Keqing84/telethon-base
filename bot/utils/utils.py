import os
import glob
import importlib

from telethon import Button
from bot.logging import LOG

class BtCrt:
    def __init__(self):
        self.btns = []

    def add_url(self, text, url):
        self.btns.append([Button.url(text, url=url)])

    def add_callback(self, text, data):
        self.btns.append([Button.inline(text, data=data)])



def load_plugins():
    for file_path in glob.glob("bot/plugins/**/*.py", recursive=True):
        module = ".".join(file_path.split("/"))[:-3]
        module_name = file_path.split("/")[-1][:-3]
        if module_name in ["__init__"]:
            continue
        try:
            importlib.import_module(module)
            LOG.info(f"Imported Module: {module_name}.py")
        except Exception as e:
            LOG.info(f"Can't Import Module {module_name}.py: {str(e)}")
