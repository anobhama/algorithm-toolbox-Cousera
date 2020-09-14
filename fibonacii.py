def calc_fib(n):
    if n <= 1:
        return n

    s = 0
    t = 1

    for _ in range(n - 1):
        s,t = t, s + t

    return t

n = int(input())
print(calc_fib(n))