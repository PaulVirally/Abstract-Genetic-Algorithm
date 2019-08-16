import random
from .Chromosome import Chromosome

def single_point(parents):
    """Single point crossover.

    Creates a new Chromosome by combining the genes of both parents. A crossover point is performed and the crossover is performed as follows:
    Parent A genes:  AAAA AAAA
    Crossover point:     ↕ 
    Parent B genes:  BBBB BBBB
                     =========
    Child:           AAAA BBBB
   
    Arguments:
        parents {[Chromosome]} -- A list containing two Chromosomes from which the genes will be taken.
    
    Returns:
        Chromosome -- The baby made from the two parents.
    """
    parents.sort(key=lambda chromo: len(chromo.genes))

    crossover_point = random.randint(0, len(parents[0].genes)-1)
    genes = parents[0].genes[:crossover_point] + parents[1].genes[crossover_point:]
    return Chromosome(genes)