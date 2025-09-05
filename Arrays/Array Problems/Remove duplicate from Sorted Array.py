# Given a sorted array arr[] of size n, the goal is to rearrange the array so that all distinct elements appear at the beginning in sorted order. Additionally, return the length of this distinct sorted subarray.

# Note: The elements after the distinct ones can be in any order and hold any value, as they don't affect the result.

# Examples: 

# Input: arr[] = [2, 2, 2, 2, 2]
# Output: [2]
# Explanation: All the elements are 2, So only keep one instance of 2.

# Input: arr[] = [1, 2, 2, 3, 4, 4, 4, 5, 5]
# Output: [1, 2, 3, 4, 5]

# Input: arr[] = [1, 2, 3]
# Output: [1, 2, 3]
# Explanation : No change as all elements are distinct.



# arr = [10, 10, 20, 30, 40, 40, 50]
# new_arr = []

# for i in range(len(arr)):
#     if arr[i] not in new_arr:
#         new_arr.append(arr[i])
    
# print(new_arr)


def remove_duplicate(ar):

    indx  = 1

    for i in range(1,len(ar)):
        if ar[i-1] != ar[i]:
            ar[indx] = ar[i]
            indx += 1
    return indx

if __name__ == '__main__':
    ar = [1,2,2,3,4,4,5,5,6]
    new_ar = remove_duplicate(ar)

    for i in range(new_ar):
        print(ar[i])




ar = [1,2,2,3,4,4,5,5,6] 

print(list(set(ar))) 



       


        




    





    
            









