def get(self,key):
    index = self.hash(key)
    
    while self.map[index] != None:
        if self.map[index].key == key:
            return self.map[index].val
        index += 1
        index = index % self.capacity
    return None