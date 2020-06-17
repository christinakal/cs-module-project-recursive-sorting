# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements

    # Your code here:
    # create 2 pointers. i will be for arrA and j for arrB
    i = 0
    j = 0
    # take the length of both arrays
    lenA = len(arrA)
    lenB = len(arrB)

    # create an empty arr (this will be the merged array)
    arr = []
    # looping throught the arrays
    while((i < lenA) and (j < lenB)):
        if(arrA[i] < arrB[j]):
            arr.append(arrA[i])
            # move to the next element of the array
            i = i + 1
        else:
            arr.append(arrB[j])
            # move to the next element of the array
            j = j + 1
    
    #  if there are remaining elements append them into the array
    while(i < lenA):
        arr.append(arrA[i])
        # move to the next element of the array
        i = i + 1
    
    while(j < lenB):
        arr.append(arrB[j])
        # move to the next element of the array
        j = j + 1
    
    return arr
   

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # split the array into half
    midpoint = len(arr) // 2
    left = arr[:midpoint]
    right = arr[midpoint:]

    if(len(left) < 2 and len(right) < 2):
        return merge(left, right)
    else:
        return merge(merge_sort(left), merge_sort(right))


# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

