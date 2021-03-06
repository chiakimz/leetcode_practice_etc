# N-ary Tree Postorder Traversal
# Given an n-ary tree, return the postorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=[]):
        self.val = val
        self.children = children

class Solution(object):
    def makeNodes(self, root):
        topNode = Node(val=root[0])
        index = 2
        for i in root[2:]:
            if i == None:
                break
            else:
                n = Node(i,[])
                topNode.children.append(n)  
        childrenArray = topNode.children        
        
        grandChildren = root[index + 1:]
        
        j = 0
        for i in grandChildren:
            if i == None:
                j = 0
                childrenArray = childrenArray.children
                break
            else:
                n = Node(i,[])
                childrenArray[j].children.append(i)

        j

    def postorder(self, root):
        self.makeNodes(root)
        """
        :type root: Node
        :rtype: List[int]
        """
        
if __name__ == "__main__":
    sol = Solution()    
    num = sol.postorder([1,None,3,2,4,None,5,6]) 
    print(str(num))        

"""
Input: root = [1,null,3,2,4,null,5,6]
Output: [5,6,3,2,4,1]
Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [2,6,14,11,7,3,12,8,4,13,9,10,5,1]
"""       