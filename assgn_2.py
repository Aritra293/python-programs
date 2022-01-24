x=input("enter string : ")
r=""
k = int(input("enter value of k = "))
for i in range(len(x)-k+1):
    num = True
for j in range(k):
    num = num & x[i + j].isdigit()
if num: 
     res =""
     for j in range(k):
         res += x[i + j]
print("required character digits:" + str(res));



