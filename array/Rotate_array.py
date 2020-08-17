class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        [1,2,3,4,5,6,7]
        """
        """
        this solution times out
            while k > 0:
            last_number = nums[len(nums)-1]
            for i in reversed(range(1,len(nums))):
                nums[i] = nums[i-1]
            nums[0] = last_number
            k = k - 1
        return nums
        """
        k = k % len(nums)
        while k > 0:
            last_number = nums.pop()
            nums.insert(0,last_number)
            k -= 1
        return nums