def fact(n):
    if n < 0:
        return "Enter non-negative numbers!"
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)

if __name__ == '__main__':
    n = int(input())
    print(fact(n))

#print(fact(100))