import random, sys

print('ROCK, PAPER, SCISSORS')

# Tracking of wins, losses and ties
wins = 0
losses = 0
ties = 0

computerMove = ()

# The main game loop
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

# The player input loop
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()      # Quit the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of the player loop
        print('Type one of the r, p, s or q.')

# Display what the player choose
    if playerMove == 'r':
        print('Rock versus ...')
    elif playerMove == 'p':
        print('Paper versus ...')
    elif playerMove == 's':
        print('Scissors versus ...')

# Display what the computer chooses
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove == 'r'
        print('Rock')
    elif randomNumber == 2:
        computerMove == 'p'
        print('Paper')
    elif randomNumber == 3:
        computerMove == 's'
        print('Scissors')

# Display and record the win/loss/tie

    if playerMove == computerMove:
        print('It is a tie')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1


        