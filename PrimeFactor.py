def largest_factor(num):
    largestprime = 0
    factor = 2  
    while factor * factor <= num:
        if num % factor == 0:
            largestprime = factor
            num //= factor
        
        factor += 1
    if num > largestprime:
        largestprime = num
    return largestprime

print(largest_factor(600851475143))
