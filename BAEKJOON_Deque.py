# 10866번
import sys
input = sys.stdin.readline

class Deque:
	def __init__(self):
		self.items = []
		self.front_index = 0
		self.rear_index = 0
	
	def push_front(self, x):
		if self.front_index == self.rear_index: # 덱이 비어있을 때
			self.rear_index += 1
			self.items.append(x)
		else: # 덱에 값이 있을 때
			self.items.append(self.items[-1])
			for i in range(len(self.items)-2, self.front_index, -1):
				self.items[i] = self.items[i-1]
			self.rear_index += 1
			self.items[self.front_index] = x
	
	def push_back(self, x):
		self.rear_index += 1
		self.items.append(x)
	
	def pop_front(self):
		if self.front_index == self.rear_index:
			return -1
		else:
			x = self.items[self.front_index]
			self.front_index += 1
			return x
	
	def pop_back(self):
		if self.front_index == self.rear_index:
			return -1
		else:
			self.rear_index -= 1
			return self.items.pop()
	
	def size(self):
		return self.rear_index - self.front_index
    
	def front(self):
		if self.front_index == self.rear_index:
			return -1
		else:
			return self.items[self.front_index]
	
	def back(self):
		if self.front_index == self.rear_index:
			return -1
		else:
			return self.items[self.rear_index - 1]
	
	def empty(self):
		if self.front_index == self.rear_index:
			return 1
		else: return 0

n = int(input())

deque = Deque()

for i in range(n):
	str = input().split()
	if len(str) == 2:
		str[1] = int(str[1])
	

	if str[0] == "push_front":
		deque.push_front(str[1])
	
	elif str[0] == "push_back":
		deque.push_back(str[1])
	
	elif str[0] == "pop_front":
		print(deque.pop_front())
	
	elif str[0] == "pop_back":
		print(deque.pop_back())
	
	elif str[0] == "size":
		print(deque.size())
	
	elif str[0] == "empty":
		print(deque.empty())
	
	elif str[0] == "front":
		print(deque.front())
	
	elif str[0] == "back":
		print(deque.back())