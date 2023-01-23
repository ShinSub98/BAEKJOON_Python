class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0
    
    def enqueue(self, val):
        self.items.append(val)
    
    def dequeue(self):
        if self.front_index == len(self.items):
            print("Queue is empty")
        else:
            x = self.items[self.front_index]
            self.front_index += 1 # 실제 삭제가 아니라 없는 취급
            return x