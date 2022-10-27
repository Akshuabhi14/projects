n=int(input())
val=ord("A")
for i in range(n):
    for j in range(n):
        if j==n//2 or i+j==n-1:
             print(chr(val),end=" ")
        else:
            print("-",end=" ")
    val+=1
    print()
