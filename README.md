# GeneticAlgorithmKnapsack
This project was developh to solve the Knapsack problem using the intuition of GeneticAlgorithm.
 
 ## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
I recomend you to use Anaconda or Miniconda package, but only what you need to install on your system are:
* Python
* Numpy

### How does it work?
You only need run the file named "main.py". Remember to make sure that all packages stay in the same folder.

Inside the "main.py" file you will see these variables:

* cross_rate
  * Percent no enable crossover fase.
* mutation_rate
  * Percent no enable mutation fase.
* max_generations
  * Define the loops of evolution.
* max_pop
  * Define the max number of single loop (generation).
* limiter
  * Limiter of values_choices (weight in knapsack).
* values_choices
  * Weight of ever possyble choice.
* reward_choices
  * Reward of ever possyble choice.
* penalty_rate

#### Examples to use
https://people.sc.fsu.edu/~jburkardt/datasets/knapsack_01/knapsack_01.html