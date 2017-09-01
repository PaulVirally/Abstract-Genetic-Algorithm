from random import choice
from Chromosome import Chromosome

class GA(object):

    def __init__(self, gene_generator_func, fitness_func, pop_size=100):
        self._gene_generator_func = gene_generator_func
        self._fitness_func = fitness_func
        self._pop_size = 100

        self._pop = []
        for __ in range(self._pop_size):
            self._pop.append(self._gene_generator_func())

    def step(self, selection_algo, crossover_algo, crossover_rate=0.3, mutation_rate=0.001):
        new_pop = []
        for __ in range(self._pop_size):
            # Selection
            pop_copy = self._pop.copy()
            for __ in range(self._pop_size):
                first = self._select(selection_algo, pop_copy)
                second = self._select(selection_algo, pop_copy)

            # Reproduction
            baby = first.reproduce(second, crossover_algo, crossover_rate, mutation_rate)

            # Fitness assessment
            baby.fitness = self._fitness_func(baby.get_dna())
            new_pop.append(baby)
        self._pop = new_pop

    def _select(self, selection_algo, pop_copy):
        if selection_algo == 'random':
            return self._random_select()
        elif selection_algo == 'random unique':
            return self._random_unique_select(pop_copy)
        else:
            print("Unknown selection function `{0}`. Aborting.".format(selection_algo))

    def _random_select(self):
        return choice(self._pop) 

    def _random_unique_select(self, pop_copy):
        chromosome = choice(pop_copy)
        pop_copy.remove(chromosome)
        return chromosome
