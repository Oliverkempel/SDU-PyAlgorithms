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

print("Input: " + str(list))
bubbleSort(list)
print("Output: " + str(list))

## Time testing yes
A = []
for i in range(10000):
    num = random.randint(0, 100)
    A.append(num)

t0 = time.time()
print("Start time: " + str(t0))
res = bubbleSort(A)
t1 = time.time()
print("End time: " + str(t1))

timeTaken = t1 - t0

print("Time taken: " + str(timeTaken))
