a=[]
b=[]
c=[]
print("\ninput for matrix\n")
m=int(input("enter rows:"))
n=int(input("enter columns:"))
for j in range(m): 
    a.append([])
    for i in range(n):
       a[j].append(int(input("enter value:")))
       
    print("\nInput for matrix 2\n")
    m=int((input("enter rows:")))
    p=int((input("enter columns:")))
    for j in range(m):
        b.append([])
        for i in range(p):
            b[j].append(int((input("enter value:"))))
            
        for j in range(m):
             c.append([])
             for i in range(n):
                c[j].append(a[j][i] + b[j][i])

        print("the sum is:")    
        for j in range(m):
            for i in range(n):
                print(str(c[j][i]),end="\t")
            print("\n")

