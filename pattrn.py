n=(1)
m=(6)
for i in range(n,m):
    for j in range(n,m):
       print("*", end =" ")
    print() 

n=(9)
for i in range(n):
    for j in range(n-i-1):
      for k in range(n-j-1):
         print("*", end =" ")
    print()  

n=(10)
for i in range(n):
    for j in range(n+1):
        print("*", end =" ")
    print()     