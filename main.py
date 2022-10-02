from ast import Not
from typing import List


print("Hello from Python")

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, data):
        # If empty list
        if self.head is None:
            self.head = ListNode(data)
            self.tail = self.head
        # If non-empty list
        else:
            self.tail.next = ListNode(data)
            self.tail = self.tail.next

def printList(headNode: ListNode):
    while headNode is not None:
        print(headNode.data, end=" ")
        headNode = headNode.next
    print()

def sumLinkedLists(list1: LinkedList, list2: LinkedList):
    outputHead = None
    sumGreaterThan10 = False
    refHead = ListNode(0)
    while list1.head is not None or list2.head is not None or sumGreaterThan10:
        list1Value = list1.head.data if list1.head else 0
        list2Value = list2.head.data if list2.head else 0
        sum = list1Value + list2Value
        if sumGreaterThan10:
            sum = sum + 1
            sumGreaterThan10 = False
        if sum > 9:
            sum = sum - 10
            sumGreaterThan10 = True
        newNode = ListNode(sum)
        if outputHead is None:
            outputHead = newNode
        if refHead.next is not None:
            refHead = refHead.next
        refHead.next = newNode
        if list1.head:
            list1.head = list1.head.next
        if list2.head:
            list2.head = list2.head.next
    return outputHead

integer1Array = [5,7,7]
integer1LinkedList = LinkedList()
for digit in integer1Array:
    integer1LinkedList.insert(digit)
integer2Array = [5,1,5]
integer2LinkedList = LinkedList()
for digit in integer2Array:
    integer2LinkedList.insert(digit)

printList(integer1LinkedList.head)
printList(integer2LinkedList.head)
resultHead = sumLinkedLists(integer1LinkedList, integer2LinkedList)
printList(resultHead)
