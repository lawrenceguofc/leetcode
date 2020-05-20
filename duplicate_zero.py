#! /usr/bin/python
class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        key point: when add, add from the end.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                for j in reversed(range(i+1,len(arr))):
                    arr[j] = arr[j-1]
                i = i + 2
            else:
                i = i + 1

def main():
    a = [1,0,2,3,0,4,5,0]
    b = [1,2,3]
    Solution().duplicateZeros(a)
    Solution().duplicateZeros(b)
    print(a)
    print(b)

if __name__ == '__main__':
    main()