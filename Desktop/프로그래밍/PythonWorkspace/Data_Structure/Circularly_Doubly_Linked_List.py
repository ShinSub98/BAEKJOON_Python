def splice (self, a, b, x):
    ap = a.prev
    bn = b.next
    xn = x.next

    ap.next = bn
    bn.prev = ap

    x.next = a
    a.prev = x
    b.next = xn
    xn.prev = b


class Node:
    def __init__(self, key = None):
        self.key = key
        self.next = self
        self.prev = self # 노드가 하나 뿐인 리스트 상태

    def __str__(self):
        return str(self.key)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.size = 0
    
    def moveAfter(self, a, x):
        splice(a, a, x)
    
    def moveBefore(self, a, x):
        splice(a, a, x.prev)
    
    def insertAfter(self, x, key):
        self.moveAfter(Node(key), x)
    
    def insertBefore(self, x, key):
        self.moveBefore(Node(key), x)
    
    def pushFront(self, key):
        self.insertAfter(self.head, key)
    
    def pushBack(self, key):
        self.insertBefore(self.head, key)
    
    def remove(self, x):
        if x == None or x == self.head:
            return "Error"
        x.prev.next = x.next
        x.next.prev = x.prev
        del x
    
    def popFront(self):
        self.remove(self.head.next)

    def popBack(self):
        self.remove(self.head.prev)
    
    def search(self, key):
        v = self.head
        while v.next != self.head:
            if v.key == key:
                return v
            v = v.next
        return "No result"
    
    def __iterator__(self):
        v = self.head
        while v.next != self.head:
            yield v
            v = v.next
    