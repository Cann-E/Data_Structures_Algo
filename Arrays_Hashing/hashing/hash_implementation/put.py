def put(self,key,val):
    index  = self.hash(key)
    
    while True :
        if self.map[index] == None:
            self.map[index] = Pair(key,val)
            self.size +=1
            if self.size >= self.capacity // 2 :
                self.rehash()
            return
        elif self.map[index].key == key:
            self.map[index].val = val
            return

        index += 1
        index = index % self.capacity