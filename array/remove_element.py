#! /usr/bin/python
class Solution:
    def removeElement(self,nums,val):
        i = 0
        while i < len(nums):
            if nums[i] == val:
                if i == len(nums) - 1:
                    nums.pop()
                else:
                    for j in range(i+1,len(nums)):
                        nums[j-1] = nums[j]
                    nums.pop()
            else:
                i = i + 1
        return nums

def main():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    s = Solution()
    s.removeElement(nums = nums,val = val)
    print(nums)

if __name__ == "__main__":
    main()