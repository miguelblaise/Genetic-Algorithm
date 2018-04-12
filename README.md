# Genetic-Algorithm
A practice project for the use of genetic algorithms.

Scenario: Suppose a sack is given to you with a specific carrying capacity. You are also given a set of items with corresponding weights and scores. The goal is for you to find the optimal combination of items that maximizes the score while being under the carrying capacity of the sack.

This genetic algorithm is designed to create a random set of items with random weights and scores. The algorithm will then group the items randomly, and sorts it by highest score. The algorithm then chooses the top half highest scoring combinations, then mixes the combinations to each other, mimicking the process of mating in biology. The children are then sorted again to get the highest score. The process is repeated multiple times to get the most optimal score for the problem. There may also be times where a mutation occurs, which increases the variability of items. A specific quirk this model has among other genetic algorithms is that for every round, the highest scoring combination is always carried over to the next round, so as to reduce the possibility of getting lower values for some iterations.
