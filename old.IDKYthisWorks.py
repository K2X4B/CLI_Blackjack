import random
deck_p = [1, 10]#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
card = 0
player_Deal = []
bank = 20 # starting amount of chips

class Deal:
    def __init__(self, ):
        self.self = self
    def deal_one(): # deals the player a card and adds it to their Deal
        card = (random.choice(deck_p))
        player_Deal.append(card)
        return player_Deal
    def deal_two(): # deals the player two cards and adds them to their Deal
        card = (random.choice(deck_p))
        player_Deal.append(card)
        card = (random.choice(deck_p))
        player_Deal.append(card)
        return player_Deal
    
class Hand:
    def __init__(self, score, cards):
        self.cards = cards
        self.score = score
        #self.bj = bj
        #self.bust = bust
    def set_cards(self):
        self.cards = cards 

cards = Deal.deal_two()
# ------------------------------

print(player_Deal)
print(cards)

hit = input("hit?")
if hit == "y":
    new_card = Deal.deal_one()
    print(new_card)  
if hit == "n":
    print(cards)

score = sum(cards)
print(score)
    







