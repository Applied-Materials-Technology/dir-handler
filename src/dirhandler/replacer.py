import json
import click
import os
import pathlib
from typing import List
import re


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

    folder_maker = FolderMaker('.', folder_data, None, None, None)
    #folder_maker.check_text("I am {a} little st{ring} with some stuff",1)
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
                 current_folder: None,
                 translation: None):  
        
        self.init_path = init_path
        self.folder_data = folder_data
        self.current_path = [init_path] 
        self.current_folder = current_folder
        self.translation = {}


        self.make_folders(self.folder_data, root=True)

        #self.print_only(self.folder_data, root=True)
        #self.check_text("I am [a] little st[ring] with some stuff",1)
        #self.check_text("I am {a} little st{ring} with some stuff",1)

    def path_edit(self, path, mode):

        """
        Adjusts paths with updated folder names
        """

        pass

    def check_text(self, filename, counterstart):

        """pseudo"""

        # Extract all substrings inside brackets
        #res = re.findall(r"\{(.*?)\}", filename)
        res = re.findall(r"\[(.*?)\]", filename)


        if bool(self.translation) == False:
            #for testing purposes
            self.translation = {"a": "REPLACE1", "ring": "REPLACE2", "COUNTING": "REPLACECOUNT", "folder_spec": "REPLACEDSPEC"}

        if bool(res) == False:

            return filename
        
        elif bool(res) == True:


            for i in res:
                #thing = "{"+str(i)+"}"
                thing = "["+str(i)+"]"
                filename = filename.replace(thing, "REPLACE")


            return filename
        

            

        

    def make_folders(self, folderdata, indent="│   ", is_last=False, root=False, counter=0):

        if isinstance(folderdata, dict):

            if root:
                path_symbol = "├──"
            else:
                path_symbol = indent + ("└── " if is_last else "├── ")
                
            for i, (key, value) in enumerate(folderdata.items()):

                last_item = (i == len(folderdata) - 1)
                
                new_indent = indent + ("    " if is_last or root else "│   ")
                if isinstance(value, (dict, list)):
                    if last_item == True:
                        new_test = self.check_text(key, counterstart=1)
                        #print(f"new test is {new_test}")
                        #print(f"key is {key}")
                        print(f"{path_symbol}{new_test}-{counter}")
                        os.mkdir(f"{key}-{counter}")
                        counternew = counter-1
                        os.chdir("..")
                    else:
                        if bool(value)==True:
                            new_test = self.check_text(key, counterstart=1)
                            #print(f"new test is {new_test}")
                            print(f"{path_symbol}{new_test}-{counter}")
                            os.mkdir(f"{key}-{counter}")
                            os.chdir(f"{key}-{counter}")
                            counternew = counter+1
                        else:
                            new_test = self.check_text(key, counterstart=1)
                            #print(f"new test is {new_test}")
                            print(f"{path_symbol}{new_test}-{counter}")
                            os.mkdir(f"{key}-{counter}")
                            counternew = counter

                    self.make_folders(value, new_indent, last_item, counter=counternew)
                else:
                    val_prefix = new_indent + ("└── " if last_item else "├── ")
                    print(f"{val_prefix}{value}.txt{counter}")
                    os.mkdir(f"{key}-{counter}")
                    os.chdir(f"{key}-{counter}")
                    with open(f"{value}.txt{counter}", "a") as f:
                        f.write(" ")
                    os.chdir("..")

    def make_folders_adjusted(self, folderdata, indent="│   ", is_last=False, root=False, counter=0):

        if isinstance(folderdata, dict):

            if root:
                path_symbol = "├──"
            else:
                path_symbol = indent + ("└── " if is_last else "├── ")
                
            for i, (key, value) in enumerate(folderdata.items()):

                last_item = (i == len(folderdata) - 1)
                
                new_indent = indent + ("    " if is_last or root else "│   ")
                if isinstance(value, (dict, list)):
                    if last_item == True:
                        myfilename = f"{path_symbol}{key}-{counter}"
                        print(self.check_text(filename=myfilename, counterstart=counter))
                        os.mkdir(f"{key}-{counter}")
                        counternew = counter-1
                        os.chdir("..")
                    else:
                        if bool(value)==True:
                            myfilename = f"{path_symbol}{key}-{counter}"
                            print(self.check_text(filename=myfilename, counterstart=counter))
                            os.mkdir(f"{key}-{counter}")
                            os.chdir(f"{key}-{counter}")
                            counternew = counter+1
                        else:
                            myfilename = f"{path_symbol}{key}-{counter}"
                            print(self.check_text(filename=myfilename, counterstart=counter))
                            os.mkdir(f"{key}-{counter}")
                            counternew = counter

                    self.make_folders(value, new_indent, last_item, counter=counternew)
                else:
                    val_prefix = new_indent + ("└── " if last_item else "├── ")
                    print(f"{val_prefix}{value}.txt{counter}")
                    os.mkdir(f"{key}-{counter}")
                    os.chdir(f"{key}-{counter}")
                    with open(f"{value}.txt{counter}", "a") as f:
                        f.write(" ")
                    os.chdir("..")


    def print_only(self, folderdata, indent="│   ", is_last=False, root=False, counter=0):

        if isinstance(folderdata, dict):

            if root:
                path_symbol = "├──"
            else:
                path_symbol = indent + ("└── " if is_last else "├── ")
                
            for i, (key, value) in enumerate(folderdata.items()):

                last_item = (i == len(folderdata) - 1)
                
                new_indent = indent + ("    " if is_last or root else "│   ")
                if isinstance(value, (dict, list)):
                    if last_item == True:
                        print(f"{path_symbol}{key}-{counter}")
                        #os.mkdir(f"{key}-{counter}")
                        counternew = counter-1
                        #os.chdir("..")
                    else:
                        if bool(value)==True:
                            print(f"{path_symbol}{key}-{counter}")
                            # os.mkdir(f"{key}-{counter}")
                            # os.chdir(f"{key}-{counter}")
                            counternew = counter+1
                        else:
                            print(f"{path_symbol}{key}-{counter}")
                            #os.mkdir(f"{key}-{counter}")
                            counternew = counter

                    self.print_only(value, new_indent, last_item, counter=counternew)
                else:
                    val_prefix = new_indent + ("└── " if last_item else "├── ")
                    print(f"{val_prefix}{value}.txt{counter}")
                    #os.mkdir(f"{key}-{counter}")
                    #os.chdir(f"{key}-{counter}")
                    # with open(f"{value}.txt{counter}", "a") as f:
                    #     f.write(" ")
                    #os.chdir("..")