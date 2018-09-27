from poker import Poker
# Your mission is to make an app that ranks poker hands of 5 cards.
# Create a stateful deck of 52 standard playing cards: 2 to Ace with the suits hearts, clubs, spades, and diamonds.
# You must be able to classify hands of 5 cards according to the offical poker hands.
# You must be able to rank 2 hands of 5 cards against each other.
# classify 5 cards according to official poker hands

def main():
    poker_game = Poker()
    player_one = raw_input('Player one playing? (y/n) ')
    player_two = raw_input('Player two playing? (y/n) ')
    if player_one == 'y' or player_one == 'Y':
        player_one_hand = poker_game.get_hand()
        player_one_rank = poker_game.classify_hand(player_one_hand)
        print('Player one: ', player_one_rank)
    if player_two == 'y' or player_two == 'Y':
        player_two_hand = poker_game.get_hand()
        player_two_rank = poker_game.classify_hand(player_two_hand)
        print('Player 2', player_two_rank)
        poker_game.compare_hands(player_one_hand, player_two_hand)

if __name__ == '__main__':
    main()
