# 4. Median of Two Sorted Arrays
# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) == 0:
            nums1 = nums2
        elif len(nums2) != 0:
            j = 0
            for i in range(len(nums1) + len(nums2)):
                if i == len(nums1) or j == len(nums2):
                    break
                called = False
                while nums1[i] <= nums2[j] and i == len(nums1) - 1 or nums1[i] <= nums2[j] and nums1[i + 1] >= nums2[j]:
                    nums1.insert(i + 1, nums2[j])
                    j += 1
                    called = True
                    if j == len(nums2):
                        break 
                        
                while  called == False and nums1[i] > nums2[j]:
                    nums1.insert(i, nums2[j])
                    j += 1
                    if j == len(nums2):
                        break                  

        med = int(len(nums1) / 2)
        if len(nums1) % 2 != 0:
            return nums1[med]
        else:
            return (nums1[med] + nums1[med - 1]) / 2.0 


if __name__ == "__main__":
    sol = Solution()    
    num = sol.findMedianSortedArrays([1, 3], [2]) 
    print(str(num))        