"""
This example will have a Genetic Algorithm converge on a word.
Each gene of a Chromosome is a letter (represented in ASCII in binary).
The fitness of a Chromosome is negative the distance each letter has to the chosen word.
"""

import sys
sys.path.insert(0, './GA')

from Chromosome import Chromosome
from GA import GA
import random

word = 'Yay!'
pop_size = 5000
pop = []
for _ in range(pop_size):
    genes = [bin(random.randrange(31, 126))[2:].zfill(7) for __ in range(len(word))]
    chromo = Chromosome(genes)
    pop.append(chromo)

def decode(chromo):
    s = ''
    for gene in chromo.genes:
        num = int(gene, 2)
        if num < 32 or num > 126:
            s += '?'
        else:
            s += chr(num)
    return s

def get_fitness(chromo):
    dist = 0
    for guess, exact in zip(chromo.genes, word):
        guess = int(guess, 2)
        exact = ord(exact)
        dist += abs(guess - exact)
    return -dist

ga = GA(pop, get_fitness, mutation_rate=0.1)

generation = 1
best = ga.get_best()
print(f'Best from generation {generation}: {decode(best)} -- Distance: {-best.fitness}')
while True:
    ga.step()
    generation += 1
    best = ga.get_best()
    decoded = decode(best)
    print(f'Best from generation {generation}: {decoded} -- Distance: {-best.fitness}')
    if decoded == word:
        break