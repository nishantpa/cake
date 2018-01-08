# << Swami Shreeji >>
# 7 Jan 2018

# Basic implementation of a linked list. PENDING

class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

	def getValue(self):
		return self.value

	def getNext(self):
		return self.next

	def setData(self, newData):
		self.data = newData

	def setNext(self, newNext):
		self.next = newNext


class UnorderedList:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

temp = Node("fjwjrvrw")
print temp.getValue()