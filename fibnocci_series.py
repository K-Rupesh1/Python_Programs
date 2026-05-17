def fibnocci(num):
    a=0
    b=1
    if num<0:
        print("incorrect input")
    elif num==0:
        return 0
    elif num==1:
        return 1
    else:
        print(a)
        print(b)
        for i in range(2,num+1):
            c=a+b
            a=b
            b=c
            print(b)
num=int(input("enter a number : "))
fibnocci(num)
        