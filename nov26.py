names=["nideesh","aritra","pranteek"]
age=[24,23,21]
subject=["ECE","CSE","EE"]
x=zip(names,age,subject)

name,a,sub=zip(*x)

print(names)
print(a)
print(sub)


a=["ccc","aa","bb"]
print(sorted(a,key=len))



l1=["eat","sleep","repeat"]

#for x,y in enumerate(l1,10):
  #print(x,y)

b="supriyo"
print(hash(b))

