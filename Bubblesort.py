import time
import random

list = [99, 7, 28, 5, 1, 2, 8, 5, 12, 4]

def bubbleSort(l):
    
    for i in range(len(l)):
        
        swaps = False
        
        for i in range(len(l) - 1):
            
            tmp0 = l[i]
            tmp1 = l[i+1]
            
            if(tmp0 > tmp1):
                l[i] = tmp1
                l[i+1] = tmp0
                swaps = True
                
        if swaps == False:
            break
        
        #print("Pass: " + str(l))
    return l

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
    res = bubbleSort(A)
    
    # End time
    t1 = time.time()
    print("End time: " + str(t1))
    print(f"Result: {res}")
    
    # Calculates time taken
    timeTaken = t1 - t0
    print("Time taken: " + f"{timeTaken:.20f}" + " milliseconds")


print("Input: " + str(list))
bubbleSort(list)
print("Output: " + str(list))

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

