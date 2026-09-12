#Day 2: 30 Days of Python programming

first_name = 'David'
last_name = 'Alderete'
full_name = 'David Alderete'
country = 'Colombia'
city = 'Bogotá'
age = 30
year = 2026
is_married = False
is_true = True
is_light_on = True
friend_name, friend_last_name, friend_age, friend_country, friend_is_married = 'Juan', 'Perez', 28, 'Colombia', False

#Checking data types
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(friend_name))
print(type(friend_last_name))
print(type(friend_age))
print(type(friend_country))
print(type(friend_is_married))

print(len(first_name))
print(len(last_name))
print(len(first_name)-len(last_name))

num_one = 5
num_two = 4
total = print('Total: ',num_one + num_two)
diff = print('Difference: ',num_two - num_one)
product = print('Product: ',num_two * num_one)
division = print('Division: ',num_one/num_two)
remainder = print('Remainder: ',num_two % num_one)
exp = print('Exponent: ',(num_one)**num_two)
floor_division = print('Floor Division: ',num_one//num_two)


circle_radius = 30
area_of_circle = print('Area of Circle: ',3.1416 * circle_radius ** 2)
circum_of_circle = print('Circumference of Circle: ',2*3.1416*circle_radius)

radius = input('Enter radius: ')
area_of_circle2 = print('Area of Circle 2: ',3.1416 * float(radius)**2)

first_name2 = str(input('Enter your first name: '))
last_name2 = str(input('Enter your last name: '))
country2 = str(input('Enter your country: '))
age2 = int(input('Enter your age: '))

