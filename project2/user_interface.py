def user_interface(options):
    '''
    function presenting options and asking for player feedback
    returns integer.
    '''
    for index, option in enumerate(options):
        print(f'{index} = {option}')

    user_input = int(input('What do you choose? '))
    return user_input