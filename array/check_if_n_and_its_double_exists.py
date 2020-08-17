#! /usr/bin/python
class Solution:
    def checkIfExist(self, arr):
        double_d = {}
        half_d = {}
        for i in range(len(arr)):
            if arr[i] in double_d:
                return True
            elif arr[i] in half_d:
                return True
            else:
                double_d[arr[i]*2] = 1
                if arr[i] % 2 == 0:
                    half_d[arr[i]/2] = 1
        return False
def main():
    arr = [10,2,5,3]
    s = Solution()
    print(s.checkIfExist(arr=arr))


if __name__ == "__main__":
    main()
