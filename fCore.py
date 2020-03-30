# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:15:44 2020

@author: Arthur
"""
import numpy as np
# Function Initialization
from fInit import initialization
# Function Score
from fScore import score
# Function GA
from fGA import ga

first_best_score_index = 0
sec_best_score_index = 0

def core(cross_rate, mutation_rate, max_generations, values_choices, choicesQtd, reward_choices, max_pop, limiter):
    first_best_score_index, sec_best_score_index, pop, score_pop = initialization(limiter, values_choices, choicesQtd, reward_choices, max_pop)
    
    first_best_score_index, sec_best_score_index, new_pop, score_new_pop = ga(pop, limiter, values_choices, choicesQtd, reward_choices, cross_rate, mutation_rate, first_best_score_index, sec_best_score_index, max_pop)
    
    for i in range(max_generations):
        first_best_score_index, sec_best_score_index, new_pop, score_new_pop = ga(new_pop, limiter, values_choices, choicesQtd, reward_choices, cross_rate, mutation_rate, first_best_score_index, sec_best_score_index, max_pop)

    return new_pop[first_best_score_index], np.take(values_choices, np.where(new_pop[first_best_score_index]==1)).sum(), np.take(reward_choices, np.where(new_pop[first_best_score_index]==1)).sum()