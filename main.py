import random
import itertools


# Deck Dictionary:
# 2 - 10 = Numbered Values
# 11 = Jack
# 12 = Queen
# 13 = King
# # 14 = Ace
# Suits:
# 1 = Spades
# 2 = Clubs
# 3 = Diamonds
# 4 = Hearts
[[3, 'Spade'], [9, 'Spade'], [7, 'Diamond']]
deck = [
    # Spades
    [2,"Spade"],[3,"Spade"],[4,"Spade"],[5,"Spade"],[6,"Spade"],[7,"Spade"],[8,"Spade"],
    [9,"Spade"],[10,"Spade"],[11,"Spade"],[12,"Spade"],[13,"Spade"],[14,"Spade"],
    # Clubs
    [2,"Club"],[3,"Club"],[4,"Club"],[5,"Club"],[6,"Club"],[7,"Club"],[8,"Club"],
    [9,"Club"],[10,"Club"],[11,"Club"],[12,"Club"],[13,"Club"],[14,"Club"],
    # Diamonds
    [2,"Diamond"],[3,"Diamond"],[4,"Diamond"],[5,"Diamond"],[6,"Diamond"],[7,"Diamond"],[8,"Diamond"],
    [9,"Diamond"],[10,"Diamond"],[11,"Diamond"],[12,"Diamond"],[13,"Diamond"],[14,"Diamond"],  
    # Hearts
    [2,"Heart"],[3,"Heart"],[4,"Heart"],[5,"Heart"],[6,"Heart"],[7,"Heart"],[8,"Heart"],
    [9,"Heart"],[10,"Heart"],[11,"Heart"],[12,"Heart"],[13,"Heart"],[14,"Heart"]
]


def main():
    card_1 = 4
    suit_1 = "Spade"
    card_2 = 3
    suit_2 = "Spade"

    in_play_deck = deck
    random.shuffle(in_play_deck)
    in_play_deck.remove([card_1, suit_1])
    in_play_deck.remove([card_2, suit_2])
    x = 0
    flops = []
    all_flops = list(itertools.combinations(in_play_deck, 3))
    
    x = 0
    for flop in all_flops:
        for card in flop:
            if card[0] == card_1 or card[0] == card_2:
                x = x + 1

    print(x/len(all_flops))
  
if __name__== "__main__":
    main()

