

def prime(num, i=2):
    # Base case: If 'i' reaches 'num', it means no divisors were found, so it's prime
    if i * i > num:
        print("The given number is a prime number")
        return True
    # Check if 'num' is divisible by 'i'
    if num % i == 0:
        print("The given number is a composite number")
        return False
    # Recursive call, incrementing 'i'
    return prime(num, i + 1)

# Example usage
prime(7)
