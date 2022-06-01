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