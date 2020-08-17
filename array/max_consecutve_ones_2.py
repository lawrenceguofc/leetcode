class Solution:
    def findMaxConsecutiveOnes(self, nums):
        a,b,c = 0,0,0
        if sum(nums) == len(nums):
            return len(nums)
        else:
            for num in nums:
                if num == 1:
                    c += 1
                else:
                    b,c = c,0
                a = max(a,b+c+1)
            return a