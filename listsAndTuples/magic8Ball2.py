import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes Definetly',
    'Reply hazy try again',
    'Ask again later :)',
    'Concentrate and ask again',
    'My reply is NO',
    'Outlook not so good',
    'Very Doubtful']

print(messages[random.randint(0, len(messages) - 1)])