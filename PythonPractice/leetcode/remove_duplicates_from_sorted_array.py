# 26. Remove Duplicates from Sorted Array

# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums):
        if nums == []:
            return None

        seen = nums[0]
        for i in nums[1:]:
            if i == seen:
                nums.remove(i)
            else:
                seen = i    
        return int(nums)


if __name__ == "__main__":
    sol = Solution()
    answer = sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) 
    print(answer) 