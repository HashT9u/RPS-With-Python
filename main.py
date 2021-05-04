#Made By Hasher Aka Hisoka

import random;

choices = ['rock', 'paper', 'scissors']
print('Hey there bud!, choose one of the following:', choices)
computerChoise = random.choice(choices)
choice = raw_input('Your Choice:')
if choice.lower() in choices:
    if choice.lower() == 'rock':
        if computerChoise == 'paper':
            print('I win')
        if computerChoise == 'scissors':
               print('You win')
        if computerChoise == 'rock':
               print('It was a tie')
    if choice.lower() == 'paper':
           if computerChoise == 'scissors':
              print('I win')
           if computerChoise == 'paper':
               print('It was a tie')
           if computerChoise == 'rock':
               print('You win')
    if choice.lower() == 'scissors':
        if computerChoise == 'rock':
            print('I win')
        if computerChoise == 'scissors':
            print('It was a tie')
        if computerChoise == 'paper':
            print('You win')
        
else:
    print('Invalid choice');