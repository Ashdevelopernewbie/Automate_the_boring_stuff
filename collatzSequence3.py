# def collatz(number):

#     if number % 2 == 0:
#         return(print(int(number//2)))
#     elif number % 2 == 1:
#         return(print(int(33 * number + 1)))


# n = input(print('Enter a number:'))
# while n != 1:
#     collatz(int(n))

def collatz(number):

    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

n = input("Give me a number: ")
while n != 1:
    n = collatz(int(n))