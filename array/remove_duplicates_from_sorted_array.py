#! /usr/bin/python
class Solution:
    def removeDuplicates(self, nums):
        d = {}
        i = 0
        while i < len(nums):
            if nums[i] in d:
                d[nums[i]] += 1
                if i == len(nums):
                    nums.pop()
                else:
                    for j in range(i+1,len(nums)):
                        nums[j-1] = nums[j]
                    nums.pop()
            else:
                d[nums[i]] = 1
                i = i + 1
        return len(nums)

def main():
    nums = [0,0,1,1,1,2,2,3,3,4]
    s = Solution()
    s.removeDuplicates(nums=nums)
    print(nums)

if __name__ == "__main__":
    main()
