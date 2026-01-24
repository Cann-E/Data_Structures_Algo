def hash(self,key):
    index = 0
    for char in key:
        index += ord(char)
    return index % self.capacity