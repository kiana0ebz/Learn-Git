from random import randint

def computer_choice(content):
    '''
    function that generates a random number based on the available options.
    returns random int
    '''
    computer_chose = randint(0, len(content) - 1)
    return computer_chose