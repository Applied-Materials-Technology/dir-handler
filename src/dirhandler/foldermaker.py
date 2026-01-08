import os
import json
import pathlib
import click
from enum import Enum

# version that can work in simple json structure case

def create_folder_structure(base_path: str, 
                            structure: dict):
    
    """
    Moves to the correct location and creates folders


    Parameters
    ----------

    base_path: str
        Path to join with the folder name to make full path of a directory to be made
    structure: dict
        The dictionary data that contains the desired directory structure
    """

    if isinstance(structure, list):
        for folder_name in structure:
            path = os.path.join(base_path, folder_name)
            os.makedirs(path, exist_ok=True)
            print(f"Created directory: {path}")
    elif isinstance(structure, dict):
        for folder_name, sub_structure in structure.items():
            path = os.path.join(base_path, folder_name)
            os.makedirs(path, exist_ok=True)
            print(f"Created directory: {path}")
            create_folder_structure(path, sub_structure)
    elif isinstance(structure, str):
        path = base_path+"/"+structure+".txt"
        f = open(path, "w")
        f.close


@click.command()
@click.option('--example', '-x', is_flag=True, help="takes example file structures when present")
@click.option('--filename', default='examples/nestedtstruc.json', help="path to json file to read structure")
@click.option('--location', default='.', help="path to create folders in")
def startclick(example,filename,location):
    
    """
    Click cimmand ot read the json structure file and call directory maker function


    Parameters
    ----------

    example: bool
        Whether the json is a premade example (True) or a unique json (False)
    filename: str
        Path to json file to read (excluding path to examples folder)
    location: str
        Where the directory structure should be made
    """

    if example == True:
        base_dir = pathlib.Path(__file__).parent.resolve() # change eventually __file__ bad...
        json_file = os.path.join(base_dir, filename)
    else:
        json_file = filename

    with open(json_file, 'r') as f:
        folder_data = json.load(f)
        print(type(folder_data))

    os.chdir(location)

    create_folder_structure('.', folder_data)
    print("Folder structure created successfully!")

def start(example = False, 
          filename = 'examples/nestedtstruc.json',
          location = '.'):

    """
    Allow for click command to be called as a function

    Parameters
    ----------

    example: bool
        Whether the json is a premade example (True) or a unique json (False)
    filename: str
        Path to json file to read (excluding path to examples folder)
    location: str
        Where the directory structure should be made
    """
    startclick.callback(example, filename, location)