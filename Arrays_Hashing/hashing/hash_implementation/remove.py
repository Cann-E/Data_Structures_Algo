def remove(self,key):
    if not self.get(key):
        return
    
    index = self.hash(key)
    
    while True:
        if self.map[index].key == key:
            self.map[index] = None
            self.size -= 1
            return
        index += 1
        index = index % self.capacity