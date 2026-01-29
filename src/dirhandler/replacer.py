import json
import click
import os
import pathlib
from typing import List

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

    os.chdir(location)

    folder_maker = FolderMaker('.', folder_data, None, None)
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

class FolderMaker():

    def __init__(self, 
                 init_path,
                 folder_data,
                 current_path: None,
                 current_folder: None):  
        
        self.init_path = init_path
        self.folder_data = folder_data
        self.current_path = init_path 
        self.current_folder = current_folder

        self.create_folder_structure(self.init_path, self.folder_data, self.current_path, self.current_folder)

    def create_folder_structure(self, initpath ,folderdata, currentpath, currentfolder):
        
        # for folder_name, sub_structure in self.folder_data.items():
        #     print(f"foldername is {folder_name}")
        #     print(f"substructure is {sub_structure}")
        #     print(f"substructure is {bool(sub_structure)}")
        #     #if type(sub_structure) is dict:
        #     #if sub_structure == True:
        #     if bool(sub_structure) == True:
        #         #self.create_folder_structure(self.init_path, sub_structure, self.current_path, self.current_folder)
        #         pass

        for foldername in self.folder_data:
            print(foldername)
            print(folderdata[foldername])
            if bool(folderdata[foldername]) is True:
                self.create_folder_structure(self.init_path, foldername, self.current_path, self.current_folder)