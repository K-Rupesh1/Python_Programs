def palindrome(s):
    i=0
    j=len(s)-1
    is_palindrome=True
    while i<j:
        if s[i]==s[j]:
            i+=1
            j-=1
            print("it is palindrome")
        else:
            is_palindrome=False
            print("not palindrome")
            break
s=input("enter a number : ")
palindrome(s)
