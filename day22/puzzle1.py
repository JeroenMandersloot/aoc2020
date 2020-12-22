def parse_deck(deck: str):
    _, cards = deck.strip().split(":\n")
    cards = list(map(int, cards.split("\n")))
    return cards


with open('input.txt', 'r') as f:
    deck_1, deck_2 = map(parse_deck, f.read().strip().split("\n\n"))


while deck_1 and deck_2:
    card_1 = deck_1.pop(0)
    card_2 = deck_2.pop(0)
    
    print(f"Player 1 players: {card_1}")
    print(f"Player 2 players: {card_2}")
    
    if card_1 > card_2:
        deck_1 += [card_1, card_2]
        print("Player 1 wins!")
    else:
        deck_2 += [card_2, card_1]
        print("Player 2 wins!")
        

winner = deck_1 if deck_1 else deck_2
score = sum(map(lambda t: t[0] * t[1], zip(winner, reversed(range(1, 1 + len(winner))))))
print(score)
        
    