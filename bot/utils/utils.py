import os
import importlib
from pathlib import Path

def load_plugins():
    plugins_folder = "plugins"

    # Iterate through files in the plugins folder
    for file_path in Path(plugins_folder).glob("*.py"):
        # Get the module name from the file name
        module_name = file_path.stem

        # Import the module dynamically
        module = importlib.import_module(f"{plugins_folder}.{module_name}")
