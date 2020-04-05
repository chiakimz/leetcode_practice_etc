# 53. Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

class Solution(object):
    def maxSubArray(self, nums):
        currentMax = max(nums)
        for i in range(len(nums)):
            for j in range(i + 1):
                currentRange = nums[j:j + len(nums) -i]
                if sum(currentRange) > currentMax:
                    currentMax = sum(currentRange)

        return currentMax

if __name__ == "__main__":
    sol = Solution()    
    res = sol.maxSubArray([-1, 2])
    print(str(res))          
        