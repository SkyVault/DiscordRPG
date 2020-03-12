from typing import List
from collections import namedtuple
from enum import Enum, auto

Path = namedtuple('Path', 'nextLoc last')

class Locs:
    MAIN_HALL=auto()
    OTHER_LOC=auto()

class Loc:
    def __init__(self, title : str, description : str, paths : List[str]):
        self.title = title
        self.description = description
        self.paths = paths

    def __str__(self):
        header = f"{self.title}"
        line = "─"*len(header)
        return f"\n\n{line}\n{header}\n{line}\n{self.description}"

class World:
    def __init__(self):
        self.theMap = {
            Locs.MAIN_HALL : Loc("Academy main hall", "A large stone hall with many pillers", [Locs.OTHER_LOC]),
            Locs.OTHER_LOC : Loc("Other location", "This is a test location", [Locs.MAIN_HALL])
        }
