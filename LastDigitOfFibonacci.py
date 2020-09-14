
n=int(input("enter the number"))
def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        print(n)

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    print( current % 10)

get_fibonacci_last_digit_naive(n)