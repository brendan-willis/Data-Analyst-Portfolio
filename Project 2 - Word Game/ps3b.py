#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 14:24:32 2023

@author: brendanwillis
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import ps2
import ps3a


word_list = ps2.load_words()

def test_mc_player(hand, N=100, seed=1):
    """
    play a hand 3 times, make sure produced same scores.
    
    """
    
    # IMPLEMENT ME
    success = True
    random.seed(seed)
    hand1 , score1 = ps3a.play_mc_hand(hand, N)
    random.seed(seed)
    hand2 , score2 = ps3a.play_mc_hand(hand, N)
    random.seed(seed)
    hand3 , score3 = ps3a.play_mc_hand(hand, N)
    test_scores = [score1, score2, score3]
    first_score = test_scores[0]
    for i in test_scores:
        if i != first_score:
            success = False
            break
            
    return success
    
    
if __name__ == "__main__":
    
    # Set the MC seed
    seed = 100
    
    test_hands = ['helloworld', 'UMasswins', 'statisticscomputing']
    for handword in test_hands:
        hand = ps2.get_frequency_dict(handword)
        if not test_mc_player(hand, N=100, seed=seed):
            print('Reproducibility problem for %s' % handword)