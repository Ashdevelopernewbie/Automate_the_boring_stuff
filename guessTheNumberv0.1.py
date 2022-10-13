# Guess the Number
# This is my take on guess the number program


print('I am thinking a number between 1 and 20')
print('Take a guess')

user_num = input()
my_num = '7'

while(my_num != user_num):
    if (my_num > user_num):
        print('Your guess is high')
    elif (my_num < user_num):
        print('Your guess is low')
    print('Bingo!')
