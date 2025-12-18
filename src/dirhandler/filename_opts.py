from dataclasses import dataclass
from typing import List

@dataclass(slots=True)
class filename_opts:

    placeholder_key: List = ["[", "]"]
