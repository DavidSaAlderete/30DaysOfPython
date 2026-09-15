age = 21 
height = 1.75
complex_number = 3 + 4j

base = float(input('Enter the base of the triangle (cm): '))
height = float(input('Enter the height of the triangle (cm): '))
area_triangle = 0.5 * base * height
print('Area of the triangle is: ', area_triangle, 'cm²')

side_a = float(input('Enter the length of side a (cm): '))
side_b = float(input('Enter the length of side b (cm): '))
side_c = float(input('Enter the length of side c (cm): '))
perimeter_triangle = side_a + side_b + side_c
print('Perimeter of the triangle is: ', perimeter_triangle, 'cm')

length = float(input('Enter the length of the rectangle (cm): '))
width = float(input('Enter the width of the rectangle (cm): '))
area_rectangle = length * width
perimeter_rectangle = 2 * (length + width)
print('Area of the rectangle is: ', area_rectangle, 'cm²')
print('Perimeter of the rectangle is: ', perimeter_rectangle, 'cm')

pi = 3.1416
radius = float(input('Enter the radius of the circle (cm): '))
area_circle = pi * radius**2
circumference_circle = 2 * pi * radius
print('Area of the circle is: ', area_circle, 'cm²')
print('Circumference of the circle is: ', circumference_circle, 'cm')

#We have the next function: y = 2x - 2
m = 2
b = -2

y_intercept = (0, b)
x_val = -b/m
x_intercept = (x_val, 0)

print('The slope of the line is: ', m)
print('The y-intercept of the line is: ', y_intercept)
print('The x-intercept of the line is: ', x_intercept)

#Finding the slope and euclidean distance between two point (2, 2) and (6, 10)
point1 = (2, 2)
point2 = (6, 10)
slope = ((point2[1] - point1[1])/(point2[0] - point1[0]))
euclidean_distance = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5

print('The slope between the points is: ', slope)
print('The euclidean distance between the points is: ', euclidean_distance)

print('The slope 1 and slope 2 are equal: ', slope == m)
print('THe slope 1 and slope 2 are not equal: ', slope != m)
print('The slope 1 is greater than slope 2: ', m > slope)
print('The slope 1 is less than slope 2: ', m < slope)
print('The slope 1 is greater than or equal to slope 2: ', m >= slope)

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is 0.
x = float(input('Enter a value for x: '))
y = x**2 +6*x + 9
print('The value of y is: ', y)

print('The length of "python" and "dragon" is not equal: ', len('python') != len('dragon'))

print('The word "on" is found in both "python" and "dragon": ', 'on' in 'python' and 'on' in 'dragon')

print('Is jargon in the sentence "I hope this course is not full of jargon"? ', 'jargon' in 'I hope this course is not full of jargon')

print('The word "on" is not found in both "python" and "dragon": ', 'on' not in 'python' and 'on' not in 'dragon')

convert_python = str(float(len('python')))
print(convert_python)

number_divisible_by_2 = int(input('Enter a number to check if it is divisible by 2: '))
print('Is the number divisible by 2? ',(number_divisible_by_2 % 2) == 0)

print('Is the floor division of 7 by 3 equal to the int converted value of 2.7? ', (7//3) == int(2.7))

print('Is the type of "10" equal to the type of 10?: ', type('10') == type(10))

print('Is int("9.8") equal to 10? ', int(float('9.8')) == 10)

hours = float(input('Enter the number of hours you work per week: '))
rate_per_hour = float(input('Enter your rate per hour: '))
weekly_earning = hours * rate_per_hour
print('Your weekly earning is: $', weekly_earning)


years_lived = int(input('Enter the number of years you have lived: '))
seconds_lived = years_lived * 365 * 24 * 60 * 60
print('You have lived for ', seconds_lived, ' seconds.')

tabla = (1, 2, 3, 4, 5)
print(f"{tabla[0]} {(tabla[0])**0} {(tabla[0]**1)} {(tabla[0]**2)} {(tabla[0]**3)}")
print(f"{tabla[1]} {(tabla[1])**0} {(tabla[1]**1)} {(tabla[1]**2)} {(tabla[1]**3)}")
print(f"{tabla[2]} {(tabla[2])**0} {(tabla[2]**1)} {(tabla[2]**2)} {(tabla[2]**3)}")
print(f"{tabla[3]} {(tabla[3])**0} {(tabla[3]**1)} {(tabla[3]**2)} {(tabla[3]**3)}")
print(f"{tabla[4]} {(tabla[4])**0} {(tabla[4]**1)} {(tabla[4]**2)} {(tabla[4]**3)}")

