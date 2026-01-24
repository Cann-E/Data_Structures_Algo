class Pair: #creating the key value pair
    def __init__(self,key,val):
        self.key = key
        self.val = val
        
class HashMap:
    def __init__(self):
        self.size = 0 #initial number of items
        self.capacity = 2 #initial capacity
        self.map = [None, None]
        
        
    def hash(self,key): #turn the each character in the word to number so when we % end find the remainder the remainder  tell us the index location for the pair to be put
        index = 0
        for c in key:
            index += ord(c) #turn the character to ascii number format for hashing
        return index % self.capacity
    
    
    def get(self,key):
        index = self.hask(key) #turn the key to ascii numbers using our hash function 
        
        while self.map[index] != None:#firsdt check is it not empty or not
            if self.map[index].key == key:#we are checking is the key  what we storing is equla to what we searching for
                return self.map[index].val #if matching we return their value
            index += 1 # we try the next index cause its not found
            index = index % self.capacity # we mod to find the new remainder to check the loop again for the other index spots
        return None #what we looking for doesnt exist so we return None
    
    
    
    def put(self,key,val):
        index = hash(key)
        
        while True: #2 oissiblites if the key we trying to insert is inside our hash map or not in ourhash map
            if self.map[index] == None: #if the spot is empty we insert the key here
                self.map[index] = Pair(key,val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.map[index].key == key: #if already the spot have the key we want to insert we just overwrite
                self.map[index].val = val
                return

            index += 1 #collision happened and its not our key we try to insert
            index = index % self.capacity #we try other indexes
            
            
            
    def rehash(self):#combination of resizze and pushback
        self.capacity = 2 * self.capacity #doubling the capacity
        newMap = []
        
        for i in range(self.capacity):#we are doubling the capacity essentialy [None] * self.capacitty
            newMap.append(None)
            
        oldMap = self.map
        self.map = newMap #the new map is the map now
        self.size = 0
        
        for pair in oldMap: #we take the variables in side the old map and move it to our map
            if pair:
                self.put(pair.key,pair.value)
        
                
                
        
            
            