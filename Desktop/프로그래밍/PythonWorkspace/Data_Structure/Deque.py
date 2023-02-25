class Deque:
    def __init__(self):
        self.items = []
        self.front_index = 0
        self.rear_index = 0

    def pushFront(self, x):
        if self.front_index == self.rear_index:
            self.rear_index += 1
            self.items.append(x)
        else:
            self.items.append(self.items[-1])
            for i in range(len(self.items)-2, self.front_index, -1):
                self.items[i] = self.items[i-1]
            self.rear_index += 1
            self.items[self.front_index] = x

    def pushBack(self, x):
        self.rear_index += 1
        self.items.append(x)
    
    def popFront(self):
        if self.front_index == self.rear_index:
            return "Deque is empty"
        else:
            x = self.items[self.front_index]
            self.front_index += 1
            return x
    
    def popBack(self):
        if self.front_index == self.rear_index:
            return "Deque is empty"
        else:
            self.rear_index -= 1
            self.items.pop()
        
    def size(self):
        return self.rear_index - self.front_index
    
    def front(self):
        if self.front_index == self.rear_index:
            return "Deque is empty"
        else:
            return self.items[self.front_index]
        
    def back(self):
        if self.front_index == self.rear_index:
            return "Deque is empty"
        else:
            return self.items[self.rear_index-1]            