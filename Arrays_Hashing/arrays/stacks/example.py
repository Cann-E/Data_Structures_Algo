def peak(self):
    return self.stack[-1]

def pop(self):
    self.stack.pop()

def push(self,num):
    self.stack.append(num)