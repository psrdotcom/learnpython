"""Factorial Solution"""


def factorial(num):
    """Factorial Function"""
    ## Tip: isinstance(0,int) returns False, which is not helping in current use case
    if type(num) != int:
        return None
    if num < 0:
        return None

    fact = 1
    if num >= 0:
        for i in range(num):
            fact = fact * (i + 1)
        return fact

in1 = int(input())
result = factorial(in1)
print(result)
