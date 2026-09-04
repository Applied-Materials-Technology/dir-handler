import dirhandler as dh
import json

translations = {"testword_list": ["one", "two", "three"], "testword":"mytestword"}

dh.json_maker.start(filename = "json_template.json", 
                    example = True, 
                    testing = True, 
                    translations = translations,
                    separator = ["-"," ","~"])


# dh.json_maker.start(filename = "json_template.json", 
#                     example = True, 
#                     testing = True, 
#                     translations = translations)

