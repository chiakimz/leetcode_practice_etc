# 21. Merge Two Sorted Lists
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None or l1.val == None:
            return l2
        elif l2 == None or l2.val == None:
            return l1
        elif (l1 == None or l1.val == None) and (l2 == None or l2.val == None):
            return None    
        else:
            # force the first node of l1 to be smaller than l2
            if l1.val > l2.val:
                l1, l2 = l2, l1

            current = l1
            temp = None
            while l1 != None:
                if l2 == None:
                    break
                if current.next == None and l2 != None:
                    if current.val > l2.val:
                        newHead = l2.next
                        temp = current
                        current = l2
                        current.next = temp
                        l2 = newHead
                        break    
                    elif current.val <= l2.val:
                        current.next = l2
                        break    

                if current.next != None and current.next.val >= l2.val:
                    newHead = l2.next
                    temp = current.next
                    current.next = l2
                    current.next.next = temp
                    l2 = newHead

                if current.next != None:
                    current = current.next 


        return l1            


if __name__ == "__main__":
    sol = Solution()
    lis1 = None
    #lis1.next = ListNode(4)
    #lis1.next.next = ListNode(4)
    lis2 = ListNode(None)
    #lis2.next = ListNode(3)
    #lis2.next.next = ListNode(4)
    answer = sol.mergeTwoLists(lis1, lis2)  
    print(answer) 