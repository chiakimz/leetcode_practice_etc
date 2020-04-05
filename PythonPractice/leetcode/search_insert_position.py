# 35. Search Insert Position
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

class Solution:
    def searchInsert(self, nums, target):
        if nums == [] or target == None:
            return None
        if target in nums:
            return nums.index(target)
        else:
            if target <= nums[0]:
                return 0    
            else:    
                for i in range(len(nums)):
                    if i == len(nums) - 1:
                        if nums[i] <= target:
                            return i + 1
                    elif nums[i] <= target and nums[i + 1] > target:
                        return i + 1
                        



if __name__ == "__main__":
    sol = Solution()
    answer = sol.searchInsert([1,3,5,6], 0) 
    print(answer)         