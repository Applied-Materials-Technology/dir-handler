import json
import os
import re
import pathlib

def parse_placeholder(key):
    """
    Checks if a key contains a placeholder

    Parameters
    ----------

    key: str
        What is to be checked for placeholders

    Returns 
    ----------

    keys: list
        List of generated names
    """
    match = re.match(r"^(.+)\[(\d+)\]$", key)
    if match:
        base_name = match.group(1)
        print(base_name)
        count = int(match.group(2))
        keys = [f"{base_name}{i}" for i in range(1, count + 1)]
    else:
        keys = [key]

    return keys


def create_structure(base_path, structure):
    """
    Recursively traverses the JSON structure and creates folders.

    Parameters
    ----------

    base_path: str
        Where to create the folders
    structure: dict
        JSON structure
    """
    if isinstance(structure, dict):
        for key, value in structure.items():
            resolved_keys = parse_placeholder(key)
            
            for folder_name in resolved_keys:
                current_path = os.path.join(base_path, folder_name)
                os.makedirs(current_path, exist_ok=True)
                
                if value:
                    create_structure(current_path, value)
                    
    elif isinstance(structure, list):

        for item in structure:
            if isinstance(item, str):
                resolved_keys = parse_placeholder(item)
                for folder_name in resolved_keys:
                    os.makedirs(os.path.join(base_path, folder_name), exist_ok=True)
            elif isinstance(item, dict):
                create_structure(base_path, item)

def start(filename, example, testing=False, translations = {}):

    if testing == True:
        path_start = "./testpath"
    else:
        path_start = "."

    if example == True:
        filepath = "src/dirhandler/examples/"
        json_template = os.path.join(filepath, filename)
    else:
        json_template = filename

    with open(json_template, 'r') as f:
        folder_data = json.load(f)
    
    #target_directory = "./my_generated_project"
    target_directory = path_start+"/my_generated_project"
    
    print(f"Generating folder structure in: {os.path.abspath(target_directory)}")
    create_structure(target_directory, folder_data)
    print("Folder structure created successfully!")


