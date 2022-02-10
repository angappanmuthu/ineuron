# 1. Write a Python program to convert kilometers to miles?

import cmath
kilometers = float(input("Enter value in kilometers: "))

# conversion factor
conv_fac = 0.621371

# calculate miles
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' % (kilometers, miles))

# 2. Write a Python program to convert Celsius to Fahrenheit?
c = int(input("Enter Celsius value: "))
f = (c * 9/5) + 32
print(f"F = {f}")

# 3. Write a Python program to display calendar?
import calendar

yy = 2017
mm = 11

# display the calendar
print(calendar.month(yy, mm))

# 4. Write a Python program to solve quadratic equation?
import cmath

a = 1
b = 4
c = 2

# calculating  the discriminant
dis = (b**2) - (4 * a*c)

# find two results
ans1 = (-b-cmath.sqrt(dis))/(2 * a)
ans2 = (-b + cmath.sqrt(dis))/(2 * a)

# printing the results
print('The roots are')
print(ans1)
print(ans2)

# 5. Write a Python program to swap two variables without temp variable?
a, b = 10, 20
print('Varaible before swap : {a},{b}')
b, a = a, b
print('Varaible after swap : {a},{b}')
print(a, b)
