def parse_deck(deck: str):
    _, cards = deck.strip().split(":\n")
    cards = list(map(int, cards.split("\n")))
    return cards


with open('input.txt', 'r') as f:
    deck_1, deck_2 = map(parse_deck, f.read().strip().split("\n\n"))


class Game:
    def __init__(self, *decks):
        self.decks = decks
    
    def play(self):
        history = set()
        deck_1, deck_2 = self.decks
        while all(map(bool, self.decks)):
            r = tuple(map(tuple, self.decks))
            if r in history:
                return 1
                
            history.add(r)
                
            card_1 = deck_1.pop(0)
            card_2 = deck_2.pop(0)
            
            winner = None
            
            if len(deck_1) >= card_1 and len(deck_2) >= card_2:
                g = Game(deck_1[:card_1], deck_2[:card_2])
                winner = g.play()
            else:
                winner = 1 if card_1 > card_2 else 2
                
            if winner == 1:
                deck_1 += [card_1, card_2]
            elif winner == 2:
                deck_2 += [card_2, card_1]
            else:
                raise ValueError(f"Unknown winner {winner}")
    
        return 1 if deck_1 else 2
    
    def compute_score(self):
        if sum(map(bool, self.decks)) != 1:
            raise ValueError("No winner has been decided yet!")
        deck = next(filter(bool, self.decks))
        return sum(map(lambda t: t[0] * t[1], zip(deck, reversed(range(1, 1 + len(deck))))))
        

game = Game(deck_1, deck_2)
winner = game.play()
print(game.compute_score())
