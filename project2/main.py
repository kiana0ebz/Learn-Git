from user_interface import user_interface
from computer_choice import computer_choice
from check_results import check_results


def play():
    print('''
    ---------------------------------
    Welcome to Rock, Paper, Scissors.
    Please pick your weapon.
    ''')

    # define the options and ask contestants to pick one
    options_list = ['Rock', 'Paper', 'Scissors']
    player_result = user_interface(options_list)
    computer_result = computer_choice(options_list)

    # visual representation in the terminal so we can see what both parties chose
    print(f'  player chose: {options_list[player_result]}')
    print(f'computer chose: {options_list[computer_result]}')

    # check the results between the two and print the winner.
    results = check_results(options_list, player_result, computer_result)
    print(f'\n{results}')


def main():
    # force the player into the play loop
    play_again = ''
    while play_again.lower() != 'n':
        play()
        print(f'Do you want to play again? ')
        play_again = input('type \'y\' for yes or \'n\' for no: ')


if __name__ == '__main__':
    main()
