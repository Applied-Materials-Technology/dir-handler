import dirhandler as dh
import json

tranlsations = {"testword": ["one", "two", "three"]}

dh.json_maker.start("json_template.json", True, True, tranlsations)