## variation 2 but this program only print upto 1 result

print('Enter a number:')
try:
    number = int(input())
except ValueError:
    print('The entered number is not an integer type.')

def collatz(number):
    while number != 1:

        if number%2==0:
            number=number/2
            return(print(int(number)))
        elif number%2==1:
            number=3*number+1
            return(print(int(number)))
        else:
            continue

collatz(number)