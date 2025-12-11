import time

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

def BinarySearch(l, key):
    if(len(l) is 0):
        return
    
    midIndex = int(len(l) / 2)
    
    print(str(midIndex)) 
    
    midEl = l[midIndex]
    if midEl == key:
        return l[int(len(l) / 2)]
    elif key > midEl:
        afterMid = l[midIndex+1:]
        print(str(afterMid))
        return BinarySearch(afterMid, key)
    elif key < midEl:
        beforeMid = l[:midIndex]
        print(str(beforeMid))
        return BinarySearch(beforeMid, key)
    else:
        return

#BinarySearch(list, 1)
print(str(BinarySearch(list, 18)))

# Time testing
maxVal = 10000
A = []
for i in range(maxVal):
    A.append(i)

t0 = time.time()
print("Start time: " + str(t0))
#res = BinarySearch(A, maxVal - 1)
t1 = time.time()
print("End time: " + str(t1))
