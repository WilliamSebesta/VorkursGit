def is_prime(n):
    if n == 0 or n == 1: return False
    if n == 2 or n == 3 or n == 5 or n == 7: return True
    
    for i in range(2, 10):
        if n % i == 0:
            return False
    
    
    return True

n = int(input("Enter a number: "))

if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
