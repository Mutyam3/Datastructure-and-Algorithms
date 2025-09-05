# Array Reverse
# Last Updated : 08 Aug, 2025
# Reverse an array arr[]. Reversing an array means rearranging the elements such that the first element becomes the last, the second element becomes second last and so on.

# Examples:

# Input: arr[] = [1, 4, 3, 2, 6, 5]  
# Output:  [5, 6, 2, 3, 4, 1]
# Explanation: The first element 1 moves to last position, the second element 4 moves to second-last and so on.

# Input: arr[] = [4, 5, 1, 2]
# Output: [2, 1, 5, 4]
# Explanation: The first element 4 moves to last position, the second element 5 moves to second last and so on.

# negative index  => [10,20,30,40,50]
#                     -5 -4 -3 -2 -1


def reverse_Array(ar):

    for i in range(0,len(ar)):
       print(ar[-(i+1)])
    

if __name__ == '__main__':
    ar = [10,20,30,40,50]
    reverse_Array(ar)


#Two pointer approach : 

ar = [10,20,30,40,50] 

left = 0
right = len(ar) - 1 

while left < right: # after swapping all at point of center left becomes greater than left so stop while loop 

    ar[left],ar[right] = ar[right], ar[left]

    left += 1 
    right -= 1 

print(ar)
