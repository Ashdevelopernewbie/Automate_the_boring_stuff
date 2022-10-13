car = ['BMW', 'Audi', 'Mercedez', 'Prada','Ford']

print('Which car do you like?')
print('1 for BMW')
print('2 for Audi')
print('3 for Mercedez')
print('4 for Prada')
print('5 for Ford')

user_input = input()

if(user_input == '1'):
    print('BMW')
elif(user_input == '2'):
    print('Audi')
elif(user_input == '3'):
    print('Mercedez')
elif(user_input == '4'):
    print('Prada')
elif(user_input == '5'):
    print('Ford')
else:
    print('Please enter value between 1 and 5')