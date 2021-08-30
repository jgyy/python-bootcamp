"""
87: Card Class
"""
from random import shuffle

SUITS = ("Hearts", "Diamonds", "Spades", "Clubs")
VALUES = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
}
RANKS = tuple(VALUES.keys())


class Card:
    """
    Card, Suit, Rank, Value
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = VALUES[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __call__(self):
        print("Dummy Card Call Method Here!")


class Deck:
    """
    Instaniate a new deck
    """

    def __init__(self):
        self.all_cards = []
        for suit in SUITS:
            for rank in RANKS:
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        """
        Shuffle the deck of cards
        """
        shuffle(self.all_cards)

    def deal_one(self):
        """
        Gives the player one card from deck
        """
        return self.all_cards.pop()


class Player:
    """
    Instaniate a new player
    """

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def __str__(self):
        return f"Player {self.name} have {len(self.all_cards)} cards."

    def remove_one(self):
        """
        Remove a card from the player hand
        """
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        """
        Add a card to the player hand
        """
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

def reset_deck():
    """
    This function resets the player cards in case the rounds are endless
    """
    player_one = Player("One")
    player_two = Player("Two")
    new_deck = Deck()
    new_deck.shuffle()
    for _ in range(26):
        player_one.add_cards(new_deck.deal_one())
        player_two.add_cards(new_deck.deal_one())
    return player_one, player_two

def main():
    """
    Main logic goes here to avoid caps variable
    """
    player_one, player_two = reset_deck()
    game_on = True
    round_num = 0
    while game_on:
        round_num += 1
        print(f"Round {round_num}")
        if round_num > 10000:
            print("Resetting to round 0")
            player_one, player_two = reset_deck()
            round_num = 0
        if len(player_one.all_cards) == 0:
            print("Player One, out of cards! Player Two Wins!")
            game_on = False
            break
        if len(player_two.all_cards) == 0:
            print("Player Two, out of cards! Player One Wins!")
            game_on = False
            break
        player_one_cards = []
        player_one_cards.append(player_one.remove_one())
        player_two_cards = []
        player_two_cards.append(player_two.remove_one())
        at_war = True
        while at_war:
            if player_one_cards[-1].value > player_two_cards[-1].value:
                player_one.add_cards(player_one_cards)
                player_one.add_cards(player_two_cards)
                at_war = False
            elif player_one_cards[-1].value < player_two_cards[-1].value:
                player_two.add_cards(player_one_cards)
                player_two.add_cards(player_two_cards)
                at_war = False
            else:
                print("WAR!")
                if len(player_one.all_cards) < 3:
                    print("Player One unable to declare war.")
                    print("PLAYER TWO WINS!")
                    game_on = False
                    at_war = False
                elif len(player_two.all_cards) < 3:
                    print("Player Two unable to declare war.")
                    print("PLAYER ONE WINS!")
                    game_on = False
                    at_war = False
                else:
                    for _ in range(3):
                        player_one_cards.append(player_one.remove_one())
                        player_two_cards.append(player_two.remove_one())
                


if __name__ == "__main__":
    main()
