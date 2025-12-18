import make_struct
import foldermaker
import json
import click
import os
import pathlib

def rewrite_path(old_path, to_replace, replacement):

    path_name = str(old_path).replace(to_replace, str(replacement))
    
    return path_name

def translate_line(base_path,
                   line,
                   placeholder_key = {"12": "ivebeenreplaced", "folder_spec": "FOLDER"}):
    
    
    path = os.path.join(base_path, line)
    for key in placeholder_key.keys():
        if str(key) in str(line):
            value = placeholder_key[key]

            if type(value) == str:
                to_replace = f"[{str(key)}]"
                path = rewrite_path(path, to_replace, str(value))

            elif type(value) == list:
                path = os.path.join(base_path, line)
                for k in value:
                    print(k)
                    to_replace = f"[{str(key)}]"
                    path = rewrite_path(path, to_replace, str(k))

            elif type(value) == int:
                path = os.path.join(base_path, line)
                for k in range(int(value)):
                    to_replace = f"[{str(key)}]"
                    path = rewrite_path(path, to_replace, str(k))
        else:
            path = os.path.join(base_path, line)

    return path

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
            path = translate_line(base_path, folder_name)
            #print(f"Created directory: {path} via list")
    elif isinstance(structure, dict):
        for folder_name, sub_structure in structure.items():
            path = os.path.join(base_path, folder_name)
            path = translate_line(base_path, folder_name)
            print(path)
            create_folder_structure(path, sub_structure)
    elif isinstance(structure, str):
        #path = base_path+"/"+structure+".txt"
        #f = open(path, "w")
        #f.close
        pass


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
        #print(type(folder_data))

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