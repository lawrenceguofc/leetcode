class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums):
            if nums[i] == 0 and i < len(nums) and sum(nums[i:])!=0:
                for j in range(i+1,len(nums)):
                    nums[j-1] = nums[j]
                nums[len(nums)-1] = 0
            else:
                i = i + 1
        return nums
                    
                
        