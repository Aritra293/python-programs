#a=42
#b=37
#def fun():
 #   global a
  #  global b
   # a=13
    #b=0
#fun()
#print(a,b)
values=[1,'a',0,False,True,'0']
filteredvalues = filter(None,values)
print("filtered elements")
for values in filteredvalues:
    print(values)

