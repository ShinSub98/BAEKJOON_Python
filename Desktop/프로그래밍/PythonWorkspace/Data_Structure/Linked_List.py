class Node:
    def __init__(self, key = None):
        self.key = key
        self.next = None
    
    def __str__(self):
        return str(self.key)


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def pushFront(self, val):
        new_Node = Node(val)
        if self.size == 0:
            self.head = new_Node
        
        else:
            tail = self.head
            while tail.next != None:
                tail = tail.next
            tail.next = new_Node
    
    def popFront(self):
        if self.size == 0:
            return "List is Empty"
        
        else:
            x = self.head
            key = x.key
            self.head = x.next
            self.size -= 1
            del x
            return key
    
    def popBack(self):
        if self.size == 0:
            return "List is Empty"
        
        else:
            if self.size == 1:
                x = self.head
                key = x.key
                self.head = self.head.next
                self.size -= 1
                del x
                return key
            else:
                prev, tail = None, self.head
                while tail.next != None:
                    prev = tail
                    tail = tail.next
                key = tail.key
                prev.next = tail.next
                self.size -= 1
                del tail
                return key
    
    def search(self, x):
        v = self.head
        while v.next != None:
            if v.key == x:
                return v
            v = v.next
        return "No result"

    def __iterator__(self):
        v = self.head
        while v.next != None:
            yield v
            v = v.next