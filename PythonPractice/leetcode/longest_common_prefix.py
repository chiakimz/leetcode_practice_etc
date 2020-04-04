# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs):
        commonLetters = ""
        
        s0 = strs[0]
        length = len(s0)  
        for l in range(length):
            if not strs or strs[l] == "":
                return ""
            for s in strs[1:]:
                what = s[:length]
                whe = s[:length] == s0
                if length > len(s) or s[:length] != s0:
                    break
            if  strs.index(s) == len(strs) - 1:
                break    
            s0 = s0[: length - 1]
            length -= 1
        return s0    


if __name__ == "__main__":
    sol = Solution()    
    res = sol.longestCommonPrefix(["qq", "qqkqqq", ""])
    print(str(res))                          
        