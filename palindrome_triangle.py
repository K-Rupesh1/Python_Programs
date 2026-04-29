'''n=5
count=0
for row in range(0,4):
    for coloumn in range(0,n):
        if row ==count and coloumn==round(n/2):
            print("*",end=" ")
            count+=1
    print()'''
#pyramid
'''n=5
for i in range (1,n+1):
    print(" "*(n-i),end=" ")
    for row in range(i,i+1):
        print("*",end=" ")
    for coloumn in range(i-1,0,-1):
        print("*",end=" ")
    print()'''

'''n=5
for i in range (1,n+1):
    print(" "*(n-i),end=" ")
    for row in range(1,i+1):
        print(row,end=" ")
    for row in range(i-1,0,-1):
        print(row,end=" ")
    print()

n = 5
for i in range(1, n + 1):
    # Print leading spaces
    print(" " * (n - i), end="")

    # Increasing part
    for j in range(1, i + 1):
        print(j, end="")

    # Decreasing part
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print() '''

n=5
for row in range(0,n+1):
    for coloumn in range(row,n):
        print("*",end=" ")
    print()

    n=5
for row in range(0,n+1):
    for coloumn in range(row,0,-1):
        print("*",end=" ")
    print()