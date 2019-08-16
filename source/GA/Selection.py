import random

def roulette_wheel(population, fitnesses, k):
    """Performs roulette wheel selection.

    The chosen individual is chosen with a probability proportional to its fitness. The higher the fitness, the greater chance the chromosome has at being chosen.
    
    Arguments:
        population {[Chromosome]} -- The population to choose from.
        fitnesses {[float]} -- The fitnesses of the population.
        k {int} -- The number of Chromosomes to choose.
    
    Returns:
        [Chromosome] -- A list of Chromosomes that were chosen.
    """
    return random.choices(population, weights=fitnesses, k=k)