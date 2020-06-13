def my_recursion(n):
    print(n)
    if n == 3:
        return
    print("Before First", n)
    my_recursion(n + 1)
    print("Before Second:", n)
    my_recursion(n + 1)
    print("Before Third:", n)
    my_recursion(n + 1)
    print("Before Fourth:", n)
    my_recursion(n + 1)
    print("After Fourth:", n)


my_recursion(1)

"""
output expected is :
1
Before First 1
2
Before First 2
3
Before Second: 2
3
Before Third: 2
3
Before Fourth: 2
3
After Fourth: 2
Before Second: 1
2
Before First 2
3
Before Second: 2
3
Before Third: 2
3
Before Fourth: 2
3
After Fourth: 2
Before Third: 1
2
Before First 2
3
Before Second: 2
3
Before Third: 2
3
Before Fourth: 2
3
After Fourth: 2
Before Fourth: 1
2
Before First 2
3
Before Second: 2
3
Before Third: 2
3
Before Fourth: 2
3
After Fourth: 2
After Fourth: 1
"""

# As each value is returned back to it's caller within the recursion loop until we have the last 4th my recursion which has no original caller other than the invocation.s

