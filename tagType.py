from enum import Enum


class tagPosition(Enum):
    front = 1
    left = 2
    top = 3
    right = 4
    bottom = 5
    back = 6


class tagInfo:
    def __init__(self, tagUID):
        self.uid = tagUID
        self.item = None
        self.tagPosition = None
        self._readUID(tagUID)

    def _readUID(self, tagUID):
        # assume UID's Form is "****" first three character represent item, and last number represent phase (0-6)
        itemName = tagUID[0:3]
        itemFunc = getattr(self, itemName, lambda: "Invalid Item")
        itemFunc()

        tagPos = tagUID[3]
        self.tagPosition = tagPosition(tagPos).name

    def tab(self):
        self.item = "table"
