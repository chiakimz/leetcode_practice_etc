# Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenStrings = []
        substrings = []
        for l in s:
            if s is None:
                return 0
            elif l in seenStrings:
                substrings.append("".join(map(str, seenStrings))) 

                ind = seenStrings.index(l)
                if len(seenStrings) == 1 or ind == len(seenStrings) - 1:
                    seenStrings = []

                else:
                    del seenStrings[0:ind + 1]    
                seenStrings.append(l)
            
            else:
                seenStrings.append(l)
        substrings.append("".join(map(str, seenStrings)))    
    
        return len(max(substrings, key=len))


if __name__ == "__main__":
    sol = Solution()    
    num = sol.lengthOfLongestSubstring("abcabcbb") 
    print(str(num))