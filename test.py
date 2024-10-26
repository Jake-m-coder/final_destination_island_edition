print('hello world')


'''
# Basic Data Types
Strings = str
Integers = int
Booleans = bool
Floats 
None

# Flow Control:
 - if
 - elif
 - else

# Loops and Conditionals:
 - for
 - while

# Conditionals
 - and
 - or
 - not
 
# Comparisons Operators
 - == # Comparison for equality
 - != # Comparison for inequality
 - >=
 - <=
 - >
 - <

'''
first_name = 'Yash'

last_name = 'Malhotra'


full_name = first_name +  ' '  + last_name

age = 13

name_plus_age = full_name + ' ' + str(age)

over_18 = False

money = 100_000_000.00

haunted = None

print(f'This is my full name: {full_name} and I am {age}'
      )

school_term = 'Half term'

if school_term == 'Now':
    print('Time for school')
elif school_term == 'Half term':
    print('half term')
else:
    print('No school')

# For loop for set number of operations

for number in range(0,101):
    # do set amount of instructions x amount of times/
    print(number)

for name in full_name:
    print(name)