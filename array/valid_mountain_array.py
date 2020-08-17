#! /usr/bin/python
class Solution:
    def validMountainArray(self, A):
        peak_index = 0
        up_direction = True
        if len(A) < 3:
            return False
        else:
            for i in range(len(A)-1):
                if up_direction:
                    if A[i+1] < A[i]:
                        up_direction = False
                        peak_index = i
                    elif A[i+1] == A[i]:
                        return False
                    else:
                        continue
                if not up_direction:
                    if A[i+1] < A[i]:
                        continue
                    else:
                        return False
            """ this part is really easy to miss. corner cases where the numbers are monotonously ascending or descending. 
             track
             """
            if peak_index == 0 or peak_index == len(A):
                    return False
            else:
                return True
def main():
    a = [0,3,2,1]
    s = Solution()
    print(s.validMountainArray(A=a))
    
if __name__ == '__main__':
    main()     