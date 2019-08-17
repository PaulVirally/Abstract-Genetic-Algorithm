from Chromosome import Chromosome
from Crossover import single_point
from Selection import roulette_wheel

class GA:
    def __init__(self, population, fitness_eval, **kwargs):
        self._fitness_eval = fitness_eval # TODO: Accept fitness_eval args and kwargs
        
        self._pop = population
        self._pop_size = len(self._pop)

        self._selection = kwargs.get('selection', roulette_wheel)
        self._num_parents = kwargs.get('num_parents', 2)

        self._crossover = kwargs.get('crossover', single_point)

        self._mutation_rate = kwargs.get('mutation_rate', 0.001)

    def step(self):
        new_pop = []
        for _ in range(self._pop_size):
            parents = self._selection(self._pop, self._num_parents)
            baby = self._crossover(parents)
            baby.mutate(self._mutation_rate)
            baby.fitness = self._fitness_eval(baby)
            new_pop.append(baby)
        self._pop = new_pop

    def get_best(self):
        self._pop.sort(key=lambda chromo: chromo.fitness, reverse=True)
        return self._pop[0]