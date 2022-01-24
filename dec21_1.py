#to find sum and difference of two lists using map()
num1 = [1, 2, 3]
num2 = [4, 5, 6]
print("Original list:")
print(num1)
print(num2)
result = map(lambda x, y: x + y, num1, num2)
result1 = map(lambda x, y: x - y, num2, num1)
print("sum and difference of two lists")
print(list(result))
print(list(result1))
