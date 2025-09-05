# Given an array arr[], the task is to generate all the possible subarrays of the given array.

# Examples: 

# Input: arr[] = [1, 2, 3]
# Output: [ [1], [1, 2], [2], [1, 2, 3], [2, 3], [3] ]

# Input: arr[] = [1, 2]
# Output: [ [1], [1, 2], [2] ] 


arr = [1,2,3] 

for i in range(0, len(arr)):
    for j in range(i,len(arr)):
       for k in range(i, j+1):
           print(arr[k], end=' ') 
       print()



 

