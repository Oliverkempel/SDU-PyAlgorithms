import time

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

def BinarySearch(l, key):
    if(len(l) is 0):
        return
    
    midIndex = int(len(l) / 2)
    
    #print(str(midIndex)) 
    
    midEl = l[midIndex]
    if midEl == key:
        return l[int(len(l) / 2)]
    elif key > midEl:
        afterMid = l[midIndex+1:]
        #print(str(afterMid))
        return BinarySearch(afterMid, key)
    elif key < midEl:
        beforeMid = l[:midIndex]
        #print(str(beforeMid))
        return BinarySearch(beforeMid, key)
    else:
        return

def TestBinarySearch(amountOfElements):
    # Creates sorted list of elements
    A = []
    for i in range(amountOfElements):
        A.append(i)

    # Start time
    t0 = time.time()
    print("Start time: " + str(t0))
    
    # Runs the search
    res = BinarySearch(A, amountOfElements - 1)
    
    # End time
    t1 = time.time()
    print("End time: " + str(t1))
    print(f"Result: {res}")
    
    # Calculates time taken
    timeTaken = t1 - t0
    print("Time taken: " + f"{timeTaken:.20f}" + " milliseconds")

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

