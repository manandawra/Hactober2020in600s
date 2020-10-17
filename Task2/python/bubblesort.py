def bubbleSort(arr):
   n = len(arr)
   # Traverse through all array elements
   for i in range(n):
       # Last i elements are already in correct position
       for j in range(0, n-i-1):
           # Swap if the element found is greater than the next element
           if arr[j] > arr[j+1] :
               arr[j], arr[j+1] = arr[j+1], arr[j]
# Driver code to test above
arr = ['t','u','t','o','r','i','a','l']
bubbleSort(arr)
print ("Sorted array is:")
for i in range(len(arr)):
    print (arr[i])
