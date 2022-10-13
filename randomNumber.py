import random

print('Do you want a random number?')
print('Yes/No (y/n)')

user_input = input()

if (user_input == 'y'):
    print('Heres a random number:')
    num = random.randint(1, 10)
    print(int(num))
else:
    print("You don't want a random number")

# this is to choose randomly from a list of word

car = ['lambo', 'bugatti', 'BMW']

print(random.choice(car))