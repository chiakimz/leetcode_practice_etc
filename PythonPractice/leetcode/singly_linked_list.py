# Solution
# Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement these functions in your linked list class:

# get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
# addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# addAtTail(val) : Append a node of value val to the last element of the linked list.
# addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
# deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
 

# Example:

# Input: 
# ["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]
# [[],[1],[3],[1,2],[1],[1],[1]]
# Output:  
# [null,null,null,null,2,null,3]

# Explanation:
# MyLinkedList linkedList = new MyLinkedList(); // Initialize empty LinkedList
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
# linkedList.get(1);            // returns 2
# linkedList.deleteAtIndex(1);  // now the linked list is 1->3
# linkedList.get(1);            // returns 3
 

# Constraints:

# 0 <= index,val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, addAtHead, addAtTail,  addAtIndex and deleteAtIndex.

class Node():
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList():
    def __init__(self, headVal):
        self.head = Node(val=headVal)
        self.length = 1

    def get(self, index):
        item = self.head
        for i in range(index):
            if item.next == None:
                return -1
            item = item.next
        return item    

        
    def addAtHead(self, val):
        currentHead = self.head
        self.head = Node(val, currentHead)
        self.length += 1
        
    def addAtTail(self, val):
        currentTail = self.get(self.length - 1)
        currentTail.next = Node(val, None)
        self.length += 1

    def addAtIndex(self, index, val):
        target = self.get(index - 1)
        if index == self.length - 1:
            target.next.next = Node(val, None)    
            self.length +=1
        elif target != -1 and target.next != None:
            newNextNext = target.next
            target.next = Node(val, newNextNext)
            self.length+= 1

    def deleteAtIndex(self, index):
        target = self.get(index - 1)
        if target != -1 and target.next != None:
            target.next = target.next.next
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:

# test below
if __name__ == "__main__":
    obj = MyLinkedList(9)
    param_1 = obj.get(0)
    obj.addAtHead(4)
    obj.addAtTail(7)
    obj.addAtTail(5)
    obj.addAtTail(2)
    obj.addAtIndex(4,6)
    obj.deleteAtIndex(3)
    obj
