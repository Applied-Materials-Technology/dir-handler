import yaml
from yaml.loader import SafeLoader
from dirhandler.json_legacy import Level
import argparse
import os

#yaml not supported

parser = argparse.ArgumentParser()
parser.add_argument("--filename", default = 'example/structureexample.yaml', type = str)
parser.add_argument("--location", default = str(os.getcwd()), type = str)

args = parser.parse_args()


def search_children(yaml_data, level_finder):

    """
    Check if children data exists, and send it to make_dir to
    write the directories
    """
    
    for i in yaml_data[0]:
        if yaml_data[0][i]:
            level_finder.deeper_dir()

            #for i in yaml_data['children']:
            for i in yaml_data[0][i]:
                search_children(i, level_finder)

            level_finder.higher_dir()

            
def read_yaml(yaml_file, level_finder):

    """
    Load the yaml file, and start initial search for 'children' folders
    """

    with open(yaml_file, 'r') as f:
        yaml_data = list(yaml.load_all(f, Loader=SafeLoader))
        print(yaml_data[0])

def start():
    level_finder = Level()
    read_yaml(args.filename, level_finder)

