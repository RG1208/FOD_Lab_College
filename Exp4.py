def maximum_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


num1 = 10
num2 = 25
num3 = 15

print("The maximum of the three numbers is:", maximum_of_three(num1, num2, num3))  


