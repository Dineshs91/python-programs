#! /usr/bin/env python

## Program for merge sort

def divide(array):
    if len(array) < 2:
        return array
    length = len(array)
    left = array[:length/2]
    right = array[length/2:]
    left = divide(left)
    right = divide(right)
    #print left, right
    sort_array = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sort_array.append(left[i])
            i += 1
        else:
            sort_array.append(right[j])
            j += 1
    while i < len(left):
        sort_array.append(left[i])
        i += 1
    while j < len(right):
        sort_array.append(right[j])
        j += 1
    return sort_array
            
def main():
    array = raw_input("Enter the numbers to be sorted:")
    array = [int(i) for i in array.split()]
    sort_array = divide(array)
    print sort_array

if __name__ == "__main__":
    main()
