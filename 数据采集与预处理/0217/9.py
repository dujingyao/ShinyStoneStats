def a(n):
    sum = 0
    for i in range(1, n + 1):
        sum *= 10
        sum += i
    print(sum % 7)


n = eval(input())
a(n)
