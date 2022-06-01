On branch feature/check_results :

def check_results(choices, player, computer):
    '''
    function that checks who won.
    returns string
    '''
    if player == computer:
        return 'It\'s a tie'
    elif (player == 0 and computer == len(choices) - 1) or (
            player > computer and not (player == len(choices) - 1 and computer == 0)):
        return 'Player Won'
    return 'Player Lost'
    
    ---------------------------------------------------------------------------
    
    On branch feature/user_interface :
    
    def user_interface(options):
    '''
    function presenting options and asking for player feedback
    returns integer.
    '''
    for index, option in enumerate(options):
        print(f'{index} = {option}')

    user_input = int(input('What do you choose? '))
    return user_input
    
    ---------------------------------------------------------------------------
    
    On branch feature/computer_choice :
    
    from random import randint


def computer_choice(content):
    '''
    function that generates a random number based on the available options.
    returns random int
    '''
    computer_chose = randint(0, len(content) - 1)
    return computer_chose
