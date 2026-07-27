import dirhandler as dh
import json

translations = {"testword": ["one", "two", "three"]}
#translations = {}

dh.json_maker.start(filename = "json_template.json", 
                    example = True, 
                    testing = True, 
                    translations = translations)