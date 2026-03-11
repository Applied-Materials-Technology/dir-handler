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
        self.current_path = [init_path] 
        self.current_folder = current_folder

        #self.create_folder_structure(self.init_path, self.folder_data, self.current_path, self.current_folder)
        #self.print_json(self.folder_data, root=True)
        self.print_testing(self.folder_data, root=True)


    def print_json(self, 
                   folderdata, 
                   indent="", 
                   is_last=True, 
                   root=False,
                   counter=0):

        if isinstance(folderdata, dict):

            if root==True:
                path_symbol = ""
            else:
                print(is_last)
                if is_last == True:
                    path_extra = "└── "
                else:
                    path_extra = "├── "
                path_symbol = indent + path_extra
                #path_symbol = indent + ("└── " if is_last else "├── ")
                
            for i, (key, value) in enumerate(folderdata.items()):
                last_item = (i == len(folderdata) - 1)
                print(f"{path_symbol}{key}")
                
                new_indent = indent + ("    " if is_last or root else "│   ")
                if isinstance(value, (dict, list)):
                    self.print_json(value, new_indent, last_item)
                else:
                    val_prefix = new_indent + ("└── " if last_item else "├── ")
                    print(f"{val_prefix}{value}")

        elif isinstance(folderdata, list):
            for i, item in enumerate(folderdata):
                last_item = (i == len(folderdata) - 1)
                new_indent = indent + ("    " if is_last else "│   ")
                
                if isinstance(item, (dict, list)):
                    self.print_json(item, new_indent, last_item)
                else:
                    print(f"{new_indent}{'└── ' if last_item else '├── '}{item}")

    def print_testing2(self, folderdata, indent="│   ", is_last=True, root=False, counter=0):

        if isinstance(folderdata, dict):

            if root:
                path_symbol = "├──"
            else:
                path_symbol = indent + ("└── " if is_last else "├── ")
                
            for i, (key, value) in enumerate(folderdata.items()):

                last_item = (i == len(folderdata) - 1)
                print(f"{path_symbol}{key}{counter}")
                #os.mkdir(f"{key}{counter}")
                
                new_indent = indent + ("    " if is_last or root else "│   ")
                if isinstance(value, (dict, list)):
                    if last_item == True:
                        counternew = counter-1 # where we would go down a directory
                        os.chdir("..")
                    counternew = counter+1 # where we would go up a directory
                    #os.chdir(f"{key}{counter}")
                    self.print_testing(value, new_indent, last_item, counter=counternew)
                else:
                    val_prefix = new_indent + ("└── " if last_item else "├── ")
                    print(f"{val_prefix}{value}.txt{counter}")


    def print_testing(self, folderdata, indent="│   ", is_last=False, root=False, counter=0):

        if isinstance(folderdata, dict):

            if root:
                path_symbol = "├──"
            else:
                path_symbol = indent + ("└── " if is_last else "├── ")
                
            for i, (key, value) in enumerate(folderdata.items()):

                last_item = (i == len(folderdata) - 1)
                print(f"{path_symbol}{key}{counter}")
                #os.mkdir(f"{key}{counter}")
                
                new_indent = indent + ("    " if is_last or root else "│   ")
                if isinstance(value, (dict, list)):
                    if last_item == True:
                        counternew = counter-1 # where we would go down a directory
                        os.chdir("..")
                    counternew = counter+1 # where we would go up a directory
                    #os.chdir(f"{key}{counter}")
                    self.print_testing(value, new_indent, last_item, counter=counternew)
                else:
                    val_prefix = new_indent + ("└── " if last_item else "├── ")
                    print(f"{val_prefix}{value}.txt{counter}")