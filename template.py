import os
from pathlib import Path
import logging
# with the help of logging i can see whatever activity my code is doing

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
# with the above i want to save some of the information
# like whenever its creating the files and folders, i want to see whether it was able to create or not
# or to observe any kind of error/exception we use this logging function

# project folder name
project_name = "ml_project"

# list of files and folders
list_of_files = [
    f"src/{project_name}/__init__.py", # with this it will create a constructor file inside the folder,const files are created when we want to store our folder as local package
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]


# how to create the above folders and files
# python logic
for filepath in list_of_files:
    filepath = Path(filepath) # this converts the path link to any machine's/ os's compatible path
    # eg: windows use '\' rather than fwd '/', so it'll change that

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # if exists dont create else create the file directory
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
    # creating file: 1st file is available or not, if avaialable then whether the file size is 0 or not
        with open (filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} already exists!")

# run command -> python template.py -> to execute this code and create the above files

# to commit changes in the github
# git add .
# git commit -m "folder structure added"
# git push origin main
