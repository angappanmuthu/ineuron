# 1. write a python code to print Hello Python

import random
print("Hello Python")

# 2. Write a Python program to do arithmetical operations addition and division.?


def add(x, y): return x+y
def div(x, y): return x/y


print(add(1, 2))
print(div(3, 9))

# 3. Write a Python program to find the area of a triangle?

b = int(input("Enter base value: "))
h = int(input("Enter height value: "))

a = (1/2) * (b * h)

print(f'Area of triangle is {a}')

# 4. Write a Python program to swap two variables?

a, b = 10, 20
print('Varaible before swap : {a},{b}')
b, a = a, b
print('Varaible after swap : {a},{b}')
print(a, b)


# 5. Write a Python program to generate a random number?

print(random.randint(9999, 10000))
