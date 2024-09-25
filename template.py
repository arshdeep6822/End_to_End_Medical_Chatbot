import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/trials.ipynb",
    "app.py",
    "store_index.py",
    "static/.gitkeep",
    "templates/chat.html",
    "test.py"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    # i need to separate my folders and files
    folder_name, file_name = os.path.split(filepath)
    
    if folder_name !="":
        os.makedirs(folder_name, exist_ok=True)
        logging.info(f"Creating Directory: {folder_name} for the file {file_name}")
    if (not os.path.exists(filepath)) or (os.path.getsize(file_name)==0):
        with open(filepath, 'w') as f:
            pass
            #logging.info(f"Creating empty file: {filename}")
    else:
        logging.info(f"{file_name} is already created")