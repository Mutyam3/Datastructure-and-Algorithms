""" Basic Problems ==> print alternates ==> Alyernate elements of an array
Given an array arr[], the task is to print every alternate element of the array starting from the first element.
 Examples :  

Input : arr[] = [10,20,30,40,50]
output : 10 30 50 
Explaination : Print the first element(10), skip the second element(20), print the third element(30), 
          skip the fourth element(40) and print the fifth element(50).

    Input : arr[] = [-5, 1, 4, 2, 12]
    Output : -5 4 12

"""

# Solution : 

arr = [int(i) for i in input('enter array:').split()] # using list comprehension 


for i in range(0,len(arr),2):
    print(arr[i])

#end of the above code 
# ------------------------------
print('------------------------------')
# using function  :

def getAlternates(ar):

    res = []

    # Iterate over all alternate elements 

    for i in range(0,len(ar),2):
        res.append(ar[i])
    return res 

if __name__ == '__main__' :
    arr = [10,20,30,40,50]
    res = getAlternates(arr)
    print(res) 








  

