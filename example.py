import dirhandler as dh
import json

# # #dh.foldermaker.start(True)

# json_file = "examples/loops.json"
# with open(json_file, 'r') as f:
#     folder_data = json.load(f)

# myloopscustom = {"x":"3", "y":"20"}
# #myloopscustom = {"x":"3", "y":[1,2,3,4]}
# myloops = dh.set_definitions(myloopscustom)

# # #dh.set_value(myloops, "x", 3)

# dh.make_struct.print_numbered(folder_data, myloops)

#dh.levels.start(True, filename='examples/nestedtstruc_replace.json')

dh.replacer.start(True, filename='examples/nestedtstruc.json')