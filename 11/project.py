"""
93: Milestone Project 2 Overview
"""
from random import shuffle

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}
ranks = tuple(values.keys())


class Card:
    """
    Card, Suit, Rank, Value
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __call__(self):
        print("Dummy Card Call Method Here!")


class Deck:
    """
    The deck start with an empty list
    """

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += f"\n {card.__str__()}"
        return f"The deck has:{deck_comp}"

    def shuffle(self):
        """
        shuffle the deck before the start of the game
        """
        shuffle(self.deck)

    def deal(self):
        """
        deal the deck of cards
        """
        return self.deck.pop()


class Hand:
    """
    Cards start with an empty list
    """

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        """
        If the card rank is ace, add to self.aces
        """
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
        return self

    def adjust_for_ace(self):
        """
        the ace value to be adjusted
        """
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    """
    Total value can be set to a default value or supplied by a user input
    """

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        """
        add chips if the bet is won
        """
        self.total += self.bet

    def lose_bet(self):
        """
        remove chips if bet is lost
        """
        self.total -= self.bet


def take_bet(chips):
    """
    Function to take bets
    """
    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except ValueError:
            print("Sorry, a bet must be an integer!")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed", chips.total)
            else:
                break


def hit(game_deck, hand):
    """
    Function that take hits
    """
    hand.add_card(game_deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(game_deck, hand, playing=True):
    """
    used the playing variable to control an upcoming while loop
    """
    while True:
        ans = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        if ans[0].lower() == "h":
            hit(game_deck, hand)
        elif ans[0].lower() == "s":
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Sorry, please try again.")
            continue
        break
    return playing


def show_some(player, dealer):
    """
    Display some cards
    """
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print("", dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep="\n ")


def show_all(player, dealer):
    """
    Display all cards
    """
    print("\nDealer's Hand:", *dealer.cards, sep="\n ")
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)


def player_busts(chips):
    """
    player lost the game
    """
    print("Player busts!")
    chips.lose_bet()


def player_wins(chips):
    """
    player wins the game
    """
    print("Player wins!")
    chips.win_bet()


def dealer_busts(chips):
    """
    dealer lost the game
    """
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(chips):
    """
    dealer wins the game
    """
    print("Dealer wins!")
    chips.lose_bet()


def push():
    """
    tie between player and dealer
    """
    print("Dealer and Player tie! It's a push.")


if __name__ == "__main__":
    while True:
        # Print an opening statement
        print(
            "Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11."
        )

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Set up the Player's chips
        player_chips = Chips()  # remember the default value is 100

        # Prompt the Player for their bet
        take_bet(player_chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        PLAYING = True
        while PLAYING:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            PLAYING = hit_or_stand(deck, player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                hit(deck, dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_chips)

            else:
                push()

        # Inform Player of their chips total
        print("\nPlayer's winnings stand at", player_chips.total)

        # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

        if new_game[0].lower() == "y":
            PLAYING = True
            continue
        print("Thanks for playing!")
        break
