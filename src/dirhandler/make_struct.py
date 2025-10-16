import json

json_file = "examples/loops.json"
with open(json_file, 'r') as f:
    folder_data = json.load(f)

myloops = {"x":"3", "y":"2"}


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
                   placeholder_key):
    """
    Loops through the json data, prints each part the specified number of times
    from the loops dictionary.
    """
    
    for i in json_struct:
        for key in placeholder_key.keys():
            if str(key) in str(i):
                value = int(placeholder_key[key])
                for k in range(value):
                    #print(f"printing {k}")
                    print(str(i).replace(str(key), str(k)))
            else:
                #print(f"{i} DOES NOT contain an {key}")
                pass


#replace_keys(folder_data, myloops)
#check_for_keys(folder_data, myloops)
#print_multi(folder_data, myloops)
print_numbered(folder_data, myloops)