import os
from pathlib import Path
import argparse
import json

# code for old json reader - works for simple case where no replacements are to occur


parser = argparse.ArgumentParser()
parser.add_argument("--filename", default = 'examples/structureexample.json', type = str)
parser.add_argument("--location", default = str(os.getcwd()), type = str)

args = parser.parse_args()

class Level():
    def __init__(self, level = 0, previouslvl = 0, directory = os.getcwd(), prev_dif = None, first_dir = True):
        self.level = level
        self.previouslvl = previouslvl
        self.directory = directory
        self.prev_dif = prev_dif
        self.first_dir = first_dir

    def deeper_dir(self):

        """
        Adds 1 to the level counter, showing a child directory
        """

        self.level = self.level + 1

    def higher_dir(self):

        """
        Substracts 1 to the level counter, showing returning to parent directory
        """

        self.level = self.level - 1

    def store_lvl(self):

        """
        Keeps the previous level so that the level difference can be calculated
        """

        self.previouslvl = self.level
    
    def get_prev_dif(self, curr_level):
        
        """
        Stores the previous level difference to determine whether a directory
        should be moved out of
        """

        self.prev_dif = curr_level

    def first_dir_switch(self):

        """
        Tracking whether or not a directory is the first directory being
        written
        """

        self.first_dir = False

def make_dir(folder_name, level_finder):

    """
    Move to the right location and create the directory
    """

    lvl_dif = level_finder.level - level_finder.previouslvl

    if level_finder.first_dir == True:
        lvl_dif = 0
        level_finder.first_dir_switch()

    print(lvl_dif)

    if lvl_dif > 0:

        for i in range(abs(lvl_dif)):
            os.makedirs(folder_name)
            os.chdir(folder_name)
            print(folder_name)

    elif lvl_dif < 0:
        for i in range(abs(lvl_dif)+1):
            os.chdir('..')
            print(os.getcwd())

        print(folder_name)
        os.makedirs(folder_name)

    elif lvl_dif == 0:
        if level_finder.prev_dif == 0:
            os.chdir("..")
        print(folder_name)
        os.makedirs(folder_name)
        os.chdir(folder_name)

    else:
        pass

    level_finder.store_lvl()
    level_finder.get_prev_dif(lvl_dif)

def search_children(json_data, level_finder):

    """
    Check if children data exists, and send it to make_dir to
    write the directories
    """

    if json_data['children']:
        level_finder.deeper_dir()

        for i in json_data['children']:
            make_dir(i['name'], level_finder)
            search_children(i, level_finder)

        level_finder.higher_dir()

def read_json(json_file, level_finder):

    """
    Load the json file, and start initial search for 'children' folders
    """

    with open(json_file) as file:
        json_data = json.load(file)
        search_children(json_data, level_finder)

def start():
    level_finder = Level()
    read_json(args.filename, level_finder)
    

