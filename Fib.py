def fib(x):
    if x in (0, 1):
        return x
    return fib(x-2) + fib(x-1)

fib_sum = 0
x = 0
while fib(x) < 4000000:
    if fib(x) % 2 == 0:
        fib_sum += fib(x)
    x += 1

print(fib_sum)
