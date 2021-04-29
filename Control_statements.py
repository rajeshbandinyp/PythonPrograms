# Control Statements examples
x=int(input("Enter X value :"))
while(x<=10):
    print(x,end=' ')
    x=x+1

if x>=0:
    print("\n")
    print("%d is the positive number"%x)
else:
    print("%d is negative number"%x)

    print("\n")
for i in range(2,10,2):
    print(i)

for i in range(5):
    if i==3:
        break
    else:
        print(i,end=" ")


