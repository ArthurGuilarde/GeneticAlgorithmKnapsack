import numpy as np

from fInit import core

cross_rate = 0.85
mutation_rate = 0.1
max_generations = 501
penalty_rate=0.9

# Maximum numbers of individuals for the population
max_pop = 200

# Max value for values_choices
limiter = 6404180

# Values for avery choice
values_choices = [382745,799601,909247,729069,467902,44328,34610,698150,823460,903959,853665,551830,610856,670702,488960,951111,323046,446298,931161,31385,496951,264724,224916,169684]
reward_choices = [825594,1677009,1676628,1523970, 943972,  97426,  69666,1296457,1679693,1902996,1844992,1049289,1252836,1319836, 953277,2067538, 675367, 853655,1826027,  65731, 901489, 577243, 466257, 369261]

# Number of possible choices. Max len of values_choices and rewarde_choices
choicesQtd =len(values_choices)




# The function core bring the best choice to do.

best, values_best, reward_best = core (cross_rate, mutation_rate, max_generations,
                                       penalty_rate, max_pop, limiter,
                                       values_choices, reward_choices, choicesQtd)


print("The best choice is: " + str(best))
print("The best value is: " + str(values_best))
print("The best reward is: " + str(reward_best))

