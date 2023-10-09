
def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]
        
        # recursion
        merge_sort(left)
        merge_sort(right)

        # initialize variables
        i = 0 # left
        j = 0 # right
        k = 0 # lst

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i+=1
            else:
                l[k] = right[j]
                j+=1
            k += 1
        
        # check if any element was left
        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1
        # check if any element was right
        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1
        
if __name__ == '__main__':

    lst = [3, 2, 1, 5, 4]
    merge_sort(lst)

    print("Sorted list is: ", lst)