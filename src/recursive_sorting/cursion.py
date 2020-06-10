def my_recursion(n):
    print(n)
    if n == 3:
        return
    my_recursion(n + 1)
    my_recursion(n + 1)


my_recursion(1)
