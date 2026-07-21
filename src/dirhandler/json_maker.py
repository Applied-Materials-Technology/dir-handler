import json
import os
import re
import pathlib

def parse_placeholder(key, tranlsations):
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

    match = re.match(r"^(.+)\[(.+)\]$", key)
    if not match:
        return [key]

    base_name = match.group(1)
    token = match.group(2)

    if token.isdigit():
        count = int(token)
        mycount = [f"{base_name}{i}" for i in range(1, count + 1)]
        return mycount
    
    else:
        count = tranlsations[token]
        mycount = [f"{base_name}{i}" for i in count]
        return mycount


def create_structure(base_path, structure, tranlsations):
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
            resolved_keys = parse_placeholder(key, tranlsations)
            
            for folder_name in resolved_keys:
                current_path = os.path.join(base_path, folder_name)
                os.makedirs(current_path, exist_ok=True)
                
                if value:
                    create_structure(current_path, value, tranlsations)
                    
    elif isinstance(structure, list):

        for item in structure:
            if isinstance(item, str):
                resolved_keys = parse_placeholder(item, tranlsations)
                for folder_name in resolved_keys:
                    os.makedirs(os.path.join(base_path, folder_name), exist_ok=True)
            elif isinstance(item, dict):
                create_structure(base_path, item, tranlsations)

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
    
    target_directory = path_start+"/my_generated_project"
    
    print(f"Generating folder structure in: {os.path.abspath(target_directory)}")
    create_structure(target_directory, folder_data, translations)
    print("Folder structure created successfully!")


