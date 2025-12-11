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
        
        print("Pass: " + str(l))

print("Input: " + str(list))
bubbleSort(list)
print("Output: " + str(list))