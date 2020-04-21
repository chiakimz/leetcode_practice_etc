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

class MyLinkedList(val=None, next=None):
    
    def __init__(self):
        self.val = val
        self.next = next
        

    def get(self, index):
        item = self
        for i in range(index + 1):
            if item.next == None:
                return -1
            item = item.next
        return item    

        
    def addAtHead(self, val):
        currentHead = self.get(0)
        newHead = MyLinkedList(val, currentHead)
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        

    def addAtTail(self, val):
        item = self 
        while item.next != None:
            item = item.next
        newTail = MyLinkedList(val, None)
        item.next = newTail    
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        

    def addAtIndex(self, index, val):
        target = self.get(index - 1)
        if target != -1 and target.next != None:
            newNextNext = target.next
            target.next = MyLinkedList(val, newNextNext)
        elif target.next.next == None:
            target.next.next = MyLinkedList(val, None)    

        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        

    def deleteAtIndex(self, index):
        target = self.get(index)
        if target != -1 and target.next != None:
            target.next = target.next.next



        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        


# Your MyLinkedList object will be instantiated and called as such:

if __name__ == "__main__":
    obj = MyLinkedList()
    param_1 = obj.get(index)
    obj.addAtHead(val)
    obj.addAtTail(val)
    obj.addAtIndex(index,val)
    obj.deleteAtIndex(index)