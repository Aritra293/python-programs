x=input("enter string :  ")
str1=""
for i in x:
      str1 = i + str1
print("original string is:", x)
print("reversed string is:",str1)
if (x == str1):
     print("it is a palindrome word")
else:
    print("not palindrome word") 