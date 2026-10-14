from dataclasses import dataclass
from typing import List
from enum import Enum


class Jsonfile(Enum):
    EXAMPLE = "json_template.json"
    PROCESSED = "processeddata.json"

def set_json(file_type):

    if file_type == "example":
        print("Found template example")
        filename = Jsonfile.EXAMPLE.value
    elif file_type == "processed":
        print("Found template processed")
        filename = Jsonfile.PROCESSED.value
    else:
        print("No template found, using example")
        filename = Jsonfile.EXAMPLE.value

    return filename