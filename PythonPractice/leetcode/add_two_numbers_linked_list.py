# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insert(self, root, item): 
        temp = ListNode(item) 
      
        if (root == None): 
            root = temp 
        else : 
            ptr = root 
            while (ptr.next != None): 
                ptr = ptr.next
            ptr.next = temp 
      
        return root 

    def arrayToList(self, arr): 
        root = None
        for i in range(len(arr)): 
            root = self.insert(root, arr[i]) 
      
        return root     

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1Array = []
        l2Array = []
        n = l1
        m = l2
        while n is not None:
            l1Array.insert(0, n.val)
            n = n.next
        while m is not None:
            l2Array.insert(0, m.val)
            m = m.next
        l1Number = int("".join(map(str, l1Array)))
        l2Number = int("".join(map(str, l2Array)))
        number = l1Number + l2Number
        res = list(map(int, str(number)))

        return self.arrayToList(res[::-1])

if __name__ == "__main__":
    sol = Solution()
    lis1 = ListNode(2)
    lis1.next = ListNode(3)
    lis1.next.next = ListNode(4)
    lis2 = ListNode(5)
    lis2.next = ListNode(6)
    lis2.next.next = ListNode(7)
    sol.addTwoNumbers(lis1, lis2)   
