list = [7, 2, 8, 5, 4]

def bubbleSort(l):
    
    for i in range(len(l)):
        
        swaps = False
        
        for i in range(len(l) - 1):
            
            el0 = l[i]
            el1 = l[i+1]
            
            if(el0 > el1):
                l[i] = el1
                l[i+1] = el0
                swaps = True
                
        if swaps == False:
            break
        
        print("Pass: " + str(l))

print("Input: " + str(list))
bubbleSort(list)
print("Output: " + str(list))