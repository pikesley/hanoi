class Pole(list):
    def __init__(self, position):
        self.position = position

    def push(self, disk):
        if len(self) > 0:
            if disk.width > self[-1].width:
                raise StackingError()
        self.append(disk)

class StackingError(Exception):
    pass
