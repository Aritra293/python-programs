#to find sum of integers using map
num1 = [11, 52, 3]
num2 = [4, 5, 16]
print("Original list:")
print(num1)
print(num2)
result = map(lambda x, y: x + y, num1, num2)
print("sum of two lists")
print(list(result))

