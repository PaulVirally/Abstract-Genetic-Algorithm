class GA:

    def __init__(self, chromo_builder, fitness_eval, pop_size):

        self._chromo_builder = chromo_builder # TODO: Accept chromo_builder args and kwargs
        self._fitness_eval = fitness_eval # TODO: Accept fitness_eval args and kwargs
        self._pop_size = pop_size

        self.pop = []
        for _ in range(self._pop_size):
            self.pop.append(_chromo_builder())