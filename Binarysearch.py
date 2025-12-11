list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

def BinarySearch(l, key):
    midIndex = int(len(l) / 2)
    midEl = l[midIndex]
    if midEl == key:
        return l[int(len(l) / 2)]
    elif key > midEl:
        afterMid = l[-midIndex:]
        print(str(afterMid))
        return BinarySearch(afterMid, key)
    elif key < midEl:
        beforeMid = l[:midIndex]
        print(str(beforeMid))
        return BinarySearch(beforeMid, key)

#BinarySearch(list, 1)
print(str(BinarySearch(list, 6)))