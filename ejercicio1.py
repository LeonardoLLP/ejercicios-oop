from typing import List

class ListOfThings():
    def __init__(self, list_of_things: List):
        self.list_of_things = list_of_things

    def get_length(self):
        return len(self.list_of_things)