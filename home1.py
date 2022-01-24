#print("john")
#type("John") 
#a=30
#print(id(a))
Name="aritra"
semester=5
age=21#
#print(Name)
#print(semester)
#print(age)
#print("camelcase")
#print("nameofstudent")
#x=y=z=50
#print(x)
#print(y)
##print(z)
#a,b,c=5,10,15
#print(a)
#print(b)
#print(c)
#a=10
#b="hi python"
#c=10.5
#print(type(a))
#print(type(b))
#print(type(c))
#a=5
#b=40.5
#c=1+3j
#print("the type of a",type(a))
#print("the type of b",type(b))
#print("c is a complex number",isinstance(1+3j,complex))
#str="string using double quotes"
#print(str)
#s = '''''A multiline
#string''' 
#print(s)
#str1="hello javatpoint"
#str2=' how are you'
#print(str1[0:2])
#print(str1[4])
#print(str1*2)
#print(str1 + str2)
#list1=[1,"hi","python",2]
#print(type(list1))
#print(list1)
#print(list1[3:])
#print(list1[0:2])
#print(list1 + list1)
#print(list1 * 3)
#tup=("hi","python",2)
#print(type((tup)))
#print(tup)

#print(tup[1:])
#print(tup[0:1])

#print(tup + tup)

#print(tup*3)

#t[2]="hi"

#d={1:'jimmy',2:'Alex',3:'john',4:'mike'}

#print(type(d))
#print(d)

#print("1st name is"+d[1])
#print("2nd name is"+d[2])

#print(d.values())
#print(d.keys())

#set1 = set()

#set2 = {'James',2,3,'python'}

#print(set2)

#set2.add(10)
#print(set2)

#set2.remove(2)
#print(set2)

#a=10
#b=0
#print('a is dividing by zero')
#assert b!=0
#print(a/b)

#def my_func(a,b,d):
 #   c=a+b+d
  #  print(c)
#my_func(10,20,40)

#a=0
#while a<4:
    #a+=1
    #if a == 2:
     #   continue
    #print(a)

#for i in range(5):
 #   if(i==3):
  #      break
   # print(i)
    #print("end of execution")

#i=18
#if(1<12):
#    print("i am less than 18") 

#n=11
#if(n%2==0):
#    print("even")
#else:
#    print("odd")

#*marks=int(input("enter the marks:"))
#if(marks>=90):
 #   print("excellent")
#elif(marks<90 and marks>=75):
 #   print("very good")
#elif(marks<75 and marks>=60):
#    print("good")
#else:
#    print("average")

#a=10
#b=12
#del a
#print(b)
#print(a)



#a = 0
#try: 
#     b = 1/a 
#except Exception as e: 
#print(e)

#a=5
#if(a>2):
 #   raise Exception('a should not exceed 2')

#a=0
#b=5
#try:
 #   c=b/a
 #   print(c)
#except Exception as e:
#    print(e)
#finally:
    #print('finally always executed')


#list=[1,2,3,4,5]
#for i in list:
    #print(i)

#a=0
#while(a<5):
 #   print(a)
  #  a=a+1

#import math
#print(math.sqrt(25))

#from math import sqrt
#print(sqrt(25))

#import calendar as cal
#print(cal.month_name[5])

#def sum(a,b):
 #   c=a+b
  #  return c
#print("the sum is:",sum(25, 15))

#x=5
#y=5

#a=[]
#b=[]
#print(x is y)
#print(a is b)

#def my_func():
#    global a
#    a=10
#    b=20
#    c=a+b
#   print(c)

#my_func()

#def func():
#   print(a)

#func()

#def outside_function():
 #   a=20
  #  def inside_function():
   #     nonlocal a
   #     a=30
    #    print("inner function:",a)
    #inside_function()
    #print("outer function:",a)
    #outside_function()
        
#def outside_function(): 
 #a = 20 
 #def inside_function(): 
 # nonlocal a 
#a = 30 
#print("Inner function: ",a) 
#inside_function() 
#print("Outer function: ",a) 
#outside_function()

#a=lambda x:x**2
#for i in range(1,6):
 #   print(a(i))
       
#def fun_generator():
 #   yield 1
 #   yield 2
 #   yield 3
    
#for value in fun_generator():
#    print(value)

#a=5+3.14j

#print(a,a.imag,a.real)

#x=(1==True)
#y=(2==False)
#z=(3==True)
#a=True + 10
#b=False + 10

#print("x is ",x)
#print("y is ",y)
#print("z is ",z)
#print("a:",a)
#print("b:",b)

#val1=10
#val2=None
#print(val1)
#print(val2)

#list=['john',678,20.4,peter]
#list1=[456,'Andrew']
#print(list)
#print(list+ list1)

#dict ={'name':'peter','age':18,'roll_nu':101}
# print(dict)

#tup =(10,20,"Dev",[2,3,4])
#print(tup)

#set={'apple','grapes','guava','papaya'}
#print(set)
#dn=int(input("enter the number:"))
#if(n%2==0):
#    print("even number")
#else:
#    print("odd number")
#print("task complete")

#a = int(input("Enter a? ")); 
#b = int(input("Enter b? ")); 
#c = int(input("Enter c? ")); 
#if a>b and a>c: 
#  print("a is largest"); 
#if b>a and b>c: 
#  print("b is largest"); 
#if c>a and c>b: 
#  print("c is largest"); 

#age=int(input("enter ur age"));
#if age>=18:
# print("u r eligible to vote");
#else:
#    print("sorry you have to wait");

#number=int(input("enter the number?"))
#if number==10:
#    print("number is equals to 10")
#elif number==50:
#  print("number is equal to 50")
#elif number==100:
#   print("number is equal to 100")
#else:
#    print("number is not equal to 10,50 or 100")
    
#marks = int(input("enter the marks?"))
#if marks>85 and marks<=100:
# print("congrats! you scored grade A")
#elif  marks>60 and marks<=85:
#    print("you scored B...")
#elif marks>40 and marks<=60:
#    print("you scored grade B...")
#elif (marks>30 and marks <=40):
#    print("you scored grade C")
#else:
#    print("sorry you failed")
    
#Iterating string using loop   
#str = "python"
#for i in str:
#     print(i)   

#prg to print the table of the given number
#list = [1,2,3,4,5,6,7,8,9,10]
#n=5
#for i in list:
    #c=n*i
   # print(c)   

#program to print the sum of the given list.
#list=[10,30,23,43,65,12]
#sum=0
#for i in list:
#    sum=sum+i
#print("the sum is:",sum)

#program to print numbers in sequence 
#for i in range(10):
    #print(i,end='')

#program to print table of given number
#n = int(input("enter the number:"))
#for i in range(1,11):
#    c=n*i
#    print(n,"*",i,"=",c)

#program to print even number using step size in range()

#n=int(input("enter the number"))
#for i in range(2,n,2):
#    print(i)


#list =['Peter','Joseph','Ricky','Devansh']
#for i in range(len(list)):
#    print("hello",list[i])

rows = int(input("Enter the rows:")) 
# Outer loop will print number of rows 
for i in range(0,rows+1): 
 # Inner loop will print number of Astrisk 
 for j in range(i): 
  print("*",end = '') 
 print()

rows =int(input("enter the rows"))
for 






    



















