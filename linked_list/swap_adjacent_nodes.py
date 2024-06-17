"""
Given a linked list, write a program to swap every two adjacent nodes and
return the modified linked list. You must solve this problem without modifying
the values in the list's nodes, only the nodes themselves may be changed.

Original list: 1 -> 2 -> 3 -> 4
After swapping: 2 -> 1 -> 4 -> 3
"""

class ListNode:
    def __init__(self, val=0,next = None):
        self.val = val
        self.next = next


def swapPairs(head):
    if head is None or head.next is None:
        return head
    temp = head.next
    head.next = swapPairs(head.next.next)
    temp.next = head

    return temp

def printList(node):
    while node:
        print(node.val, end="->" if node.next else "\n")
        node = node.next


def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next

    return head

arr = [1, 2, 3, 4]
head = createLinkedList(arr)
print("Original list:")
printList(head)

# Swap pairs
swapped_head = swapPairs(head)
print("After swapping:")
printList(swapped_head)