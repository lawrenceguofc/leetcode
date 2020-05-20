#! /usr/bin/python
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        Input:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3
        Output: [1,2,2,3,5,6]
        """
        last,i,j = m+n-1,m-1,n-1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[last] = nums1[i]
                i = i - 1
                last = last - 1
            else:
                nums1[last] = nums2[j]
                j = j - 1
                last = last - 1
        while j >=0:
            nums1[last] = nums2[j]
            last = last - 1
            j = j - 1
def main():
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    m = 3
    n = 3
    Solution().merge(nums1,m,nums2,n)
    print(nums1)


if __name__ == '__main__':
    main()

