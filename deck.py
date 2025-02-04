import random

deal = ""
deck = []
player_hand = []

class Card:
    def __init__(self, value, suite,):

        self.value = value
        self.suite = suite

CA = Card(1, "club")
C2 = Card(2, "club")
C3 = Card(3, "club")
C4 = Card(4, "club")
C5 = Card(5, "club")
C6 = Card(6, "club")
C7 = Card(7, "club")
C8 = Card(8, "club")
C9 = Card(9, "club")
C10 = Card(10, "club")
CJ = Card(10, "club")
CQ = Card(10, "club")
CK = Card(10, "club")

DA = Card(1, "diamond")
D2 = Card(2, "diamond")
D3 = Card(3, "diamond")
D4 = Card(4, "diamond")
D5 = Card(5, "diamond")
D6 = Card(6, "diamond")
D7 = Card(7, "diamond")
D8 = Card(8, "diamond")
D9 = Card(9, "diamond")
D10 = Card(10, "diamond")
DJ = Card(10, "diamond")
DQ = Card(10, "diamond")
DK = Card(10, "diamond")

HA = Card(1, "heart")
H2 = Card(2, "heart")
H3 = Card(3, "heart")
H4 = Card(4, "heart")
H5 = Card(5, "heart")
H6 = Card(6, "heart")
H7 = Card(7, "heart")
H8 = Card(8, "heart")
H9 = Card(9, "heart")
H10 = Card(10, "heart")
HJ = Card(10, "heart")
HQ = Card(10, "heart")
HK = Card(10, "heart")

SA = Card(1, "spade")
S2 = Card(2, "spade")
S3 = Card(3, "spade")
S4 = Card(4, "spade")
S5 = Card(5, "spade")
S6 = Card(6, "spade")
S7 = Card(7, "spade")
S8 = Card(8, "spade")
S9 = Card(9, "spade")
S10 = Card(10, "spade")
SJ = Card(10, "spade")
SQ = Card(10, "spade")
SK = Card(10, "spade")

   
deck = [CA, C2, C3, C4, C5, C6, C7, C8, C9, C10, CJ, CQ, CK, DA, D2, D3, D4, D5, D6, D7, D8, D9, D10, DJ, DQ, DK, SA, S2, S3, S4, S5, S6, S7, S8, S9, S10, SJ, SQ, SK, HA, H2, H3, H4, H5, H6, H7, H8, H9, H10, HJ, HQ, HK]

def Deal(self, deal):
    
    self.deal = input("y/n")
    if deal == "y":
        card = (random.choice(deck))
        player_hand.append(card)
        print(player_hand)
        deal = "n"

Deal(player_hand)