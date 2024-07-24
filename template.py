import os 
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "textSummarizer"

list_of_file = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'main.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb'
]

# Creating these folders and files
for fp in list_of_file:
    # Convert the path into specified os format
    fp = Path(fp)
    filedir, filename = os.path.split(fp)

    # Checking if file directory is not empty
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        # what exist_ok=True does it will not create the folder if it already exists
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    # First check whether the file exists or not or if the file size is 0 then only create the file
    if (not os.path.exists(fp)) or (os.path.getsize(fp) == 0):
        with open(fp, 'w') as f:
            pass # Since we only want to create the file, simply passing it
        logging.info(f"Creating empty file: {fp}")
    else:
        logging.info(f"{filename} already exists!!!!")
