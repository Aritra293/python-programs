# Program to find intersection of two arrays

arr1 = [1, 2, 4, 6, 7]
arr2 = [2, 3, 5, 6]
result = list(filter(lambda x: x in arr1, arr2))
print ("Intersection : ",result)
