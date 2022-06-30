import random


def play():
    user = input(
        "What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    comp = random.choice(['r', 'p', 's'])

    if user == comp:
        return print('It\'s a tie')

    elif is_win(user, comp) == True:
        return print("You win!")

    return print("You lose")


def is_win(player, opponent):
    # return true if the player wins
    # r > s, s > p , p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


play()
