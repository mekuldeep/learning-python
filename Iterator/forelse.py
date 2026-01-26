def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return f"This is not a prime number {num}"
    else:
        return f"This is prime number {num}"
        

print(is_prime(int(input("Please Enter a number : "))))