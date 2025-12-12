import json
from typing import List

"""

json_file = "examples/loops.json"
with open(json_file, 'r') as f:
    folder_data = json.load(f)

myloops = {"x":"3", "y":"2"}"""


def replace_keys(json_struct,
                 placeholder_key):
    for i in json_struct:
        #print(i)
        res = i.translate(str.maketrans(myloops))
        print(res)

def check_for_keys(json_struct,
                   placeholder_key):
    """
    Says if a value exists in each value in a json
    """
    for i in json_struct:
        for key in placeholder_key.keys():
            if key in i:
                print(f"{i} contains an {key}")
            else:
                print(f"{i} DOES NOT contain an {key}")

def print_multi(json_struct, 
                placeholder_key):
    
    for i in json_struct:
        for key in placeholder_key.keys():
            if str(key) in str(i):
                value = int(placeholder_key[key])
                for k in range(value):
                    print(f"printing {k}")
            else:
                print(f"{i} DOES NOT contain an {key}")

def print_numbered(json_struct,
                   placeholder_key={}):
    """
    Loops through the json data, and either:
    prints each part the specified number of times from the loops dictionary.
    or prints each part and replaces it with entries of a given list
    """
    
    for i in json_struct:
        for key in placeholder_key.keys():
            if str(key) in str(i):
                value = placeholder_key[key]
                if type(value) == list:
                    for k in value:
                        print(str(i).replace(str(key), str(k)))
                else:
                    for k in range(int(value)):
                        print(str(i).replace(str(key), str(k)))
            else:
                pass
            
def translate_line(line,
                   placeholder_key = {}):
        
    for key in placeholder_key.keys():
        if str(key) in str(line):
            value = placeholder_key[key]
            if type(value) == list:
                for k in value:
                    print(str(line).replace(str(key), str(k)))
            else:
                for k in range(int(value)):
                    print(str(line).replace(str(key), str(k)))
        else:
            pass
        

def set_value(dictionary, 
              name, 
              definition):
    
    dictionary[name] = definition

def set_definitions(dictionary=None):
    default_dictionary = {"x":"3", "y":"2"}
    if dictionary == None:
        dictionary = default_dictionary
    else:
        #for i in dictionary:
        #    default_dictionary[i] = dictionary[i]
        #dictionary = default_dictionary
        #not sure why above exists... keep in case breaks for now
        dictionary = dictionary

    return dictionary