import numpy as np

from fCore import core

cross_rate = 0.85
mutation_rate = 0.1
max_generations = 1001

# Maximum numbers of individuals for the population
max_pop = 20


# Max value for values_choices
limiter = 165

# Values for avery choice
values_choices = [23,   31,   29,   44,   53,   38,   63,   85,   89,   82]
reward_choices = [92,   57,   49,   68,   60,   43,   67,   84,   87,   72]

# Number of possible choices. Max len of values_choices and rewarde_choices
choicesQtd =len(values_choices)

# The function core bring the best choice to do.
best, values_best, reward_best = core(cross_rate, mutation_rate, max_generations, values_choices, choicesQtd, reward_choices, max_pop, limiter)

print("The best choice is: " + str(best))
print("The best value is: " + str(values_best))
print("The best reward is: " + str(reward_best))
