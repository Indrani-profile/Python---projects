import random

class DeckOfCards:
    def __init__(self):
        self.deck = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for rank in range(2, 11):
                self.deck.append(f"{rank} of {suit}")
            for face_card in ["Jack", "Queen", "King"]:
                self.deck.append(f"{face_card} of {suit}")
            self.deck.append(f"Ace of {suit}")

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if not self.is_empty():
            return self.deck.pop()
        else:
            return None

    def is_empty(self):
        return len(self.deck) == 0

def calculate_hand_value(hand):
    value = 0
    num_aces = 0

    for card in hand:
        if card.startswith("Ace"):
            num_aces += 1
        elif card.startswith(("King", "Queen", "Jack")):
            value += 10
        else:
            value += int(card.split()[0])

    while num_aces > 0 and value + 11 <= 21:
        value += 11
        num_aces -= 1

    return value

def main():
    deck = DeckOfCards()
    deck.shuffle()

    player_hand = [deck.deal(), deck.deal()]
    dealer_hand = [deck.deal(), deck.deal()]

    print(f"Player's hand: {', '.join(player_hand)}")
    print(f"Dealer's hand: {dealer_hand[0]}, [Hidden Card]")

    if calculate_hand_value(player_hand) == 21:
        print("Player has blackjack! Player wins.")
        return

    while True:
        action = input("Do you want to [H]it or [S]tand? ").strip().lower()

        if action == "h":
            player_hand.append(deck.deal())
            print(f"Player's hand: {', '.join(player_hand)}")
            player_value = calculate_hand_value(player_hand)

            if player_value > 21:
                print("Player busts! Dealer wins.")
                return
        elif action == "s":
            break

    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.deal())

    print(f"Dealer's hand: {', '.join(dealer_hand)}")
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21:
        print("Dealer busts! Player wins.")
    elif dealer_value > calculate_hand_value(player_hand):
        print("Dealer wins.")
    elif dealer_value < calculate_hand_value(player_hand):
        print("Player wins.")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()