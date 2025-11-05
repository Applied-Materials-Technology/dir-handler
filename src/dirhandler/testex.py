import dirhandler as dh
import json

#dh.foldermaker.start(True)

json_file = "examples/loops.json"
with open(json_file, 'r') as f:
    folder_data = json.load(f)

myloopscustom = {"x":"3", "y":"20"}
myloops = dh.set_definitions(myloopscustom)

#dh.set_value(myloops, "x", 10)

dh.make_struct.print_numbered(folder_data, myloops)
