# to store intermediate results
dict = {}


def fact(n):
    if n < 0:
        return "Enter non-negative numbers!"
    if n in dict:
        return dict[n]
    if n == 1 or n == 0:
        return 1
    else:
        factorial = fact(n-1) * n
        dict[n] = factorial
        return factorial


if __name__ == '__main__':
    n = int(input())
    print(fact(n))

#print(fact(100))