import json
import os
import re
import pathlib
import click

def parse_placeholder(key, translations, separator):
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
        mycount = [f"{base_name}{separator[0]}{i}" for i in range(1, count + 1)]
        return mycount
    
    else:
        try:
            count = translations[token]
            if type(count) == str:
                mycount = [f"{base_name}{separator[1]}{count}"]
                return mycount
            elif type(count) == list:
                mycount = [f"{base_name}{separator[2]}{i}" for i in count]
                return mycount
        except KeyError:
            return [key]
        
def create_structure(base_path, structure, translations, separator):
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
            resolved_keys = parse_placeholder(key, translations, separator)
            
            for folder_name in resolved_keys:
                current_path = os.path.join(base_path, folder_name)
                os.makedirs(current_path, exist_ok=True)
                
                if value:
                    create_structure(current_path, value, translations, separator)
                    
    elif isinstance(structure, list):

        for item in structure:
            if isinstance(item, str):
                resolved_keys = parse_placeholder(item, translations, separator)
                for folder_name in resolved_keys:
                    os.makedirs(os.path.join(base_path, folder_name), exist_ok=True)
            elif isinstance(item, dict):
                create_structure(base_path, item, translations, separator)


@click.command()
@click.option('--filename', default='json_template.json', help="path to json file to read structure")
@click.option('--example', '-x', is_flag=True, help="takes example file structures when present")
@click.option('--testing', '-t', is_flag=True, help="takes example file structures when present")
@click.option('--translations', default={}, help="dictionary of translations for placeholders")
@click.option('--separator', default=["","",""], help="What to seperate default and placeholder names with. Order - int, str, list")
def startclick(filename, example=False, testing=False, translations = {}, separator=["","",""]):

    if type(translations) == str:
        translations = json.loads(translations)

    if type(separator) == str:
        separator = [separator, separator, separator]
    elif type(separator) == list:
        if len(separator) == 1:
            separator = [separator[0], separator[0], separator[0]]
        if len(separator) == 2:
            separator = [separator[0], separator[1], separator[1]]


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
    create_structure(target_directory, folder_data, translations, separator)
    print("Folder structure created successfully!")

def start(filename="testfile", example=False, testing=False, translations = {}, separator=["","",""]):

    startclick.callback(filename, example, testing, translations, separator)

