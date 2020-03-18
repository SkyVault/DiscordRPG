from typing import List
from collections import namedtuple
from enum import Enum, auto
from reloadr import autoreload

Path = namedtuple('Path', 'nextLoc last')

@autoreload
class Locs(str, Enum):
    MAIN_HALL="Main Hall"
    OTHER_LOC="Other Loc"

@autoreload
class Loc:
    def __init__(self, title : str, description : str, paths : List[str]):
        self.title = title
        self.description = description
        self.paths = paths

    def __str__(self):
        header = f"{self.title}"
        line = "─"*len(header)

        paths = f"You can go\n"
        for path in self.paths:
            nextLoc = Map.DATA[path]
            paths += f"- {nextLoc.title}\n"

        return f"{line}\n{header}\n{line}\n{self.description}\n{paths}"

class Map:
    DATA = {
        "Main Hall" : Loc("Main Hall", "A large stone hall with many pillers", ["Other Loc", "Bathroom"]),
        "Other Loc" : Loc("Other Loc", "This is a test location", ["Main Hall"]),
        "Bathroom"  : Loc("Bathroom", "The bathroom looks like it hasn't been cleaned in years", ["Main Hall", "Computer Room"]),
        "Computer Room"  : Loc("Computer Room", "This is the room for computers", ["Bathroom"])
    }

    def __getitem__(self, key):
        return self.DATA[key]

    def __getattr__(self, attr):
        return self.DATA[attr]

class World:
    def __init__(self):
        self.theMap = Map.DATA
