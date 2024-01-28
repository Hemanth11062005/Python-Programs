#fibonnacci series using generators

def fib(limit):
    a, b = 0, 1
    while a<limit:
        yield a
        a, b = b, a+b

x = fib(6)

for i in fib(6+1):
    print(i)