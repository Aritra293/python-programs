x=5
y="tissue"
print(x)
print(y)
a=6
b=11
print(a+b)
x=("apple")
print(x)
print(type(x))

thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

myset = {"apple", "banana", "cherry"}
print(type(myset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)



thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

  thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)


thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

set1 = {"a","b","c"}
set2 = {1,2,3}

set3 = set1.union(set2)
print(set3)

set1 = {"aritra","eshan","james"}
set2 = {4,5,6}

set4 = set1.update(set2)
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print(z)

x.symmetric_difference_update(y)

print(x)

student={
"katha":"nagarbazar",
"anchita":"Baguihati",
"indranil":"Kestopur"
}
print(student["anchita"])
print(student.get("katha"))
print(student.values())
student["katha"]="barasat"
print(student)

student.update({"Sayan":"Bagmari"})
print(student)
student["Pritam"]="bagbazar"
print(student)
student.update({"Aritra":"Phoolbagan"})
print(student)

student.popitem()
print(student)
del student["indranil"]
print(student)

for x,y in student.items():
 print(x,y)

str1=input("enter your key")
st2=input("enter value")
student[str1]=st2
print(student)

