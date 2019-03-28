import pandas as pd
import numpy as np

# define poker hand
def check_poker_hand(all_hands):
    poker_hands = {'Nothing in Hand': 0, 'One Pair': 0, 'Two Pairs': 0,  'Three of a Kind' : 0, 'Straight' : 0, 'Flush' : 0, 'Full House' : 0, 'Straight Flush': 0, 'Royal Flush' : 0}
    
    poker_occ_hands = np.zeros(9)
    for hand in all_hands:
        poker_occ_hands[hand - 1]  += 1
    return poker_occ_hands


df = pd.read_csv('poker_testing.csv')
df_test = pd.read_csv('poker_training.csv')

all_hands = df_test.iloc[0:5, -1].tolist()

print(check_poker_hand(all_hands))


