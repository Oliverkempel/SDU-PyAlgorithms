import time
import random

def mergeSort(arr):
    length = len(arr)
    if length <= 1:
        return arr
    mid = length // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]
    
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left,right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]< right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def TestBinarySearch(amountOfElements):
    # Creates list of random elements
    A = []
    for i in range(amountOfElements):
        num = random.randint(0, 100)
        A.append(num)

    # Start time
    t0 = time.time()
    print("Start time: " + str(t0))
    
    # Runs the search
    res = mergeSort(A)
    
    # End time
    t1 = time.time()
    print("End time: " + str(t1))
    print(f"Result: {res}")
    
    # Calculates time taken
    timeTaken = t1 - t0
    print("Time taken: " + f"{timeTaken:.20f}" + " milliseconds")


arr = [38, 27, 43, 3, 9, 82, 10]
sortedArr = mergeSort(arr)
print("Given array is", arr)
print("Sorted array is", sortedArr)

print("=======[ Test for 10 elements ]=======")
TestBinarySearch(10)
print()

print("=======[ Test for 1000 elements ]=======")
TestBinarySearch(1000)
print()

print("=======[ Test for 1000000 elements ]=======")
TestBinarySearch(1000000)
print()

print("=======[ Test for 1000000000 elements ]=======")
TestBinarySearch(1000000000)
print()
