import random

# ================== CARD ==================
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


# ================== DECK ==================
class Deck:
    def __init__(self):
        self.cards = []
        ranks = ['2', '3', '4', '5', '6', '7', '8',
                 '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop()  # loại trừ (không trùng)
        return None


# ================== HAND ==================
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        if card:
            self.cards.append(card)

    def show(self):
        for card in self.cards:
            print(card)


# ================== PLAYER ==================
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def draw(self, deck):
        card = deck.deal()
        self.hand.add_card(card)

    def show_hand(self):
        print(f"\n{self.name}'s hand:")
        self.hand.show()


# ================== GAME ==================
class PokerGame:
    def __init__(self):
        self.deck = Deck()
        self.players = []

    def start(self):
        self.deck.shuffle()

        n = int(input("Số người chơi: "))
        for i in range(n):
            name = input(f"Tên người chơi {i+1}: ")
            self.players.append(Player(name))

    def deal_cards(self):
        for _ in range(5):  # mỗi người 5 lá
            for p in self.players:
                p.draw(self.deck)

    def show_all(self):
        for p in self.players:
            p.show_hand()


# ================== MAIN ==================
if __name__ == "__main__":
    game = PokerGame()
    game.start()
    game.deal_cards()
    game.show_all()