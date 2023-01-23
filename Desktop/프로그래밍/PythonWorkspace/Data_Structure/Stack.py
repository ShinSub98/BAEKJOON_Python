class Stack:
    def init(self):
        self.items=[]

    def push(self, val): #push
        self.items.append(val)
    
    def pop(self): #pop
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is Empty")
    
    def top(self): #top
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is Empty")
    
    def __len__(self):
        return len(self.items)