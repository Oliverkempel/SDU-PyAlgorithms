def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -1

mylist = [6, 4, 1, 9, 7, 3, 2, 8]
x = 3

result = linearSearch(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")