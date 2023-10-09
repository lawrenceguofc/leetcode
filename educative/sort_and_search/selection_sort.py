


def selection_sort(l):
    """
    maintain two lists
    1. sublist of already sorted elements
    2. sublist of remaining unsorted
    """
    for i in range(len(l)):
        min_index = i
        for j in range(i+1,len(l)):
            if l[min_index] > l[j]:
                    min_index = j
        l[i], l[min_index] = l[min_index], l[i]


if __name__ == '__main__':

    lst = [3, 2, 1, 5, 4]
    selection_sort(lst)  # Calling selection sort function

    # Printing Sorted lst
    print("Sorted lst: ", lst)
