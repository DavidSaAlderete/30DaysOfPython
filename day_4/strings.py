word = ['Thirty', 'Days', 'Of', 'Python']
word_concatenated = ' '.join(word)
print(f'{word[0]} {word[1]} {word[2]} {word[3]}')
print(word_concatenated)

word_2 = ['Coding', 'For', 'All']
word_2_concatenated = ' '.join(word_2)
print(word_2_concatenated)

company = ('Coding For All')
print(company)
print(len(company))

company_upper = company.upper()
print(company_upper)

company_lower = company.lower()
print(company_lower)

company_capitalize = company.capitalize()
print(company_capitalize)

company_title = company.title()
print(company_title)

company_swapcase = company.swapcase()
print(company_swapcase)

company_cut = company[7:]
print(company_cut)

indexing = company.index('Coding')
print(indexing)

finding = company.find('All')
print(finding)

replace = company.replace('Coding', 'Python')
print(replace)

word_3 = 'Python For Everyone'
replace_2 = word_3.replace('Everyone', 'All')
print(replace_2)

word_3_split = word_3.split(' ')
print(word_3_split)

companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
companies_split = companies.split(', ')
print(companies_split)

print(company[0])
last_index = len(company) - 1
print(company[last_index])
print(last_index)

print(company[10])

abbreviation = 'Python For Everyone'
print( abbreviation[0], abbreviation[7], abbreviation[11])

print("The abbreviation #2 is: ", company[0], company[7], company[11], "--->", company)

print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))

print("Finding the word 'because' in the next sentence: 'You cannot end a sentence with because because because is a conjunction'")
word_because = 'You cannot end a sentence with because because because is a conjunction'
print(word_because.index('because'))
print(word_because.rindex('because'))
print(word_because.find('because'))
print(word_because.rfind('because'))

first_letter = (word_because.find('because because because'))
last_letter = first_letter + len('because because because')
print(word_because[first_letter:last_letter])
print(len('because because because'))
                    

print(word_because.find('because'))

print(company.startswith('Coding'))
print(company.endswith('coding'))

phrase = '   Coding For All      '
print(phrase.strip())
print(phrase)

python_libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' #'.join(python_libraries))

print('I am enjoying this challenge. \n I just wonder what is next')

print('Name\tAge\tCountry\tCity')
print('David\t0\tCanada\tVancouver')

radius = 10
area = 3.14 * radius**2
print(f'The area of a circle with radius {radius} is {area} meter square')

a = 8
b = 6

print(f'{a} + {b} =', a + b)
print(f'{a} - {b} =', a - b)
print(f'{a} * {b} =', a * b)
print(f'{a} / {b} =', f'{(a / b):.2f}')
print(f'{a} % {b} =', a % b)
print(f'{a} // {b} =', a // b)
print(f'{a} ** {b} =', a ** b)