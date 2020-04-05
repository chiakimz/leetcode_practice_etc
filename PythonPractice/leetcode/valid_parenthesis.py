# 20. Valid Parentheses
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        char_pair = {"{" : "}", "[" : "]", "(" : ")" }    
        found = []
        for ch in s:
            if ch in char_pair:
                found.append(char_pair[ch])
            elif not found:
                return False    
            elif ch == found[-1]:
                found.pop(-1)
            else:
                return False   
        if found:
            return False
        else:
            return True              


if __name__ == "__main__":
    sol = Solution()    
    res = sol.isValid(")")
    print(str(res))            