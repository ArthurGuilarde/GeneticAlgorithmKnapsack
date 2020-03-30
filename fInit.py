# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:03:07 2020

@author: Arthur
"""
import numpy as np

from fScore import score

def initialization(limiter, values_choices, choicesQtd, reward_choices, max_pop):
    for i in range (max_pop):
        if i ==0:
            pop = np.array([np.random.randint(2, size=choicesQtd)])
        else:
            individuo = np.array([np.random.randint(2, size=choicesQtd)])
            pop = np.append(pop, individuo, axis=0)

    score_pop = score(pop, values_choices, reward_choices, limiter)


    first_best_score_index = np.where(score_pop==-np.sort(-score_pop)[0])[0][0]
    # first_best_score = pop[first_best_score_index]

    sec_best_score_index = np.where(score_pop==-np.sort(-score_pop)[1])[0][0]
    # sec_best_score = pop[sec_best_score_index]

    return first_best_score_index, sec_best_score_index, pop, score_pop