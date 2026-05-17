def prime_number(n):

    if n <= 1:
        print("Not a prime number")

    else:
        is_prime = True

        for i in range(2, n):

            if n % i == 0:
                is_prime = False
                break

        if is_prime:
            print("Prime number")
        else:
            print("Not a prime number")


n = int(input("Enter a number: "))
prime_number(n)



def print_prime_numbers(n):

    for num in range(2, n + 1):

        is_prime = True

        for i in range(2, num):

            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)


n = int(input("Enter a number: "))
print_prime_numbers(n)