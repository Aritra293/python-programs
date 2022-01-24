x=['1','2','3','4']
y=['A','B','C','D']
zipped=zip(x,y)
list_result=list(zipped)
print(list_result)
a,b=zip(*list_result)
print("a =",a)
print("b=",b)
