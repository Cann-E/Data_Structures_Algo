class prefix:
    def __init__(self,nums):
        self.prefix=[]
        total=0
        
        for n in nums:
            total +=n
            self.prefix.append(total)
            
            
    def rangesum(self,left,right):
        preright = self.prefix[right]
        preleft = self.prefix[left-1] if left > 0 else 0
        return (preright - preleft)