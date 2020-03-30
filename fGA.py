# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:15:44 2020

@author: Arthur
"""
import numpy as np
from fScore import score


def ga(pop, limiter, values_choices, choicesQtd, reward_choices, cross_rate, mutation_rate, first_best_score_index, sec_best_score_index, max_pop):
    # Get the best 2 individuals of previous generetion
    new_pop = [pop[first_best_score_index]]
    new_pop = np.append(new_pop, [pop[sec_best_score_index]], axis=0)


    # Generante and fill new_pop until max_pop value
    for i in range(int((max_pop - 2)/2)):
        # Select 2 random individuals of pop
        a = np.random.randint(0, max_pop)
        b = np.random.randint(0, max_pop)

        # Choosing at random the crossing process
        if cross_rate >= np.random.random(1):
            # Choosing at random cut point
            cut = np.random.randint(1, choicesQtd)

            # A pieces
            a_p1 = pop[a, 0:cut]
            a_p2 = pop[a, cut:]

            # B pieces
            b_p1 = pop[b, 0:cut]
            b_p2 = pop[b, cut:]

            # Crossover part
            new_a = np.append(a_p1, b_p2)
            new_b = np.append(b_p1, a_p2)

            # Choosing at random mutation point
            if mutation_rate >= np.random.random(1):

                mutation_a = np.random.randint(1, choicesQtd)
                mutation_b = np.random.randint(1, choicesQtd)

                # Applying mutation in a
                if(new_a[mutation_a] == 1):
                    new_a[mutation_a] = 0
                else:
                    new_a[mutation_a] = 1

                # Applying mutation in b
                if(new_b[mutation_b] == 1):
                    new_b[mutation_b] = 0
                else:
                    new_b[mutation_b] = 1
        

            # Add in new_pop
            new_pop = np.append(new_pop, [new_a], axis=0)
            new_pop = np.append(new_pop, [new_b], axis=0)

        else:
           new_pop = np.append(new_pop, [pop[a]], axis=0)
           new_pop = np.append(new_pop, [pop[b]], axis=0)

    score_new_pop = score(new_pop, values_choices, reward_choices, limiter)

    first_best_score_index = np.where(score_new_pop==-np.sort(-score_new_pop)[0])[0][0]

    sec_best_score_index = np.where(score_new_pop==-np.sort(-score_new_pop)[1])[0][0]

    return first_best_score_index, sec_best_score_index, new_pop, score_new_pop