# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

class Solution:
    def longestCommonPrefix(self, strs):
        commonLetters = ""
        if not strs or strs[0] == "":
            return ""

        # Find common prefixes in the first two strings

        for s in range(len(strs[0])):
            if len(strs) == 1:
                return strs[0]
            else:    
                if s == len(strs[1]):
                    break
                if strs[0][s] == strs[1][s]:  
                    commonLetters += strs[0][s]
                else:
                    break
        if not commonLetters:
            return ""     

        #since first two are already checked, start from the index 2
        if len(strs) > 2:
            for i in range(2, len(strs)):
                if strs[i] == "":    
                    return ""
                else:    
                    for s in range(len(commonLetters)):
                        if s == len(strs[i]):
                            break
                        if commonLetters[s] != strs[i][s]:
                            commonLetters = commonLetters[:s]    
                            break
                        elif commonLetters[s] == strs[i][s] and s == len(strs[i]) - 1:
                            commonLetters = commonLetters[:s + 1]  
                            break

        return commonLetters

if __name__ == "__main__":
    sol = Solution()    
    res = sol.longestCommonPrefix(["qq", "qqkqqq", ""])
    print(str(res))                          
        