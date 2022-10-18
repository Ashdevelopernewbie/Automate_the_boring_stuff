## This is my version of Collatzseq

# function that define whether a number is even or odd
def collatz(num):
    if num%2==0:
        print(num // 2)
        return(num // 2)
    elif num % 2 == 1:
        result = 3 * num + 1
        print(result)
        return(result)



# num = 0
# num = input(print('Give a number.'))
# if num != 1:
#     collatz(num)
# else:
#     print('The End')

userNum = input('Give a number.')
while userNum != 1:
    userNum = collatz(int(userNum))


