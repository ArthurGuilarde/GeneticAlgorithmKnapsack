# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:03:07 2020

@author: Arthur
"""
import numpy as np

def score(pop, values_choices, reward_choices, limiter, penalty_rate=0.1):

    score_pop = []

    if penalty_rate > 0.5:
       penalty_rate = 0.5

    for i in pop:
        indexEscolhas = np.where(i ==1)[0]
        score = np.take(reward_choices, indexEscolhas).sum()

        if  np.take(values_choices, indexEscolhas).sum() > limiter:
            score = score  * penalty_rate

        score_pop.append(score)


    return np.array(score_pop)

