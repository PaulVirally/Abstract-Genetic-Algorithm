class Chromosome(object):
    """Chromosome class for a genetic algorithm.
    
    This class represents a chromosome which is the individual that is being
    "evolved" in a genetic algorithm.
    """
    def __init__(self, genes):
        """Chromosome constructor.
        
        Args:
            genes: A list of strings, each string being a binary number
                   representing a specific gene (or trait) of the
                   chromosome.
        """
        self._genes = genes
        self._fitness = float('-inf')

    def _mutate(self, mutation_rate=0.001):
        """Mutates the choromosome to add some randomness to the evolution
        process.
        
        This will flip any bit in the chromosome's genes with a probability
        equal to `mutattion_rate`.
        
        Args:
            mutation_rate: The probability that any bit of any of the
            chromosome's genes will flip (default: 0.001). The reason this is 
            a parameter of this function and not a parameter of the constructor
            of the class, is to allow a varying mutation rate which might be 
            desired in some situations.
        """
        new_genes = []
        for gene in self._genes:
            new_gene = ''
            for bit in gene:
                if random() <= mutation_rate:
                    new_gene += '1' if bit == '0' else '0' # Flips the bit
                else:
                    new_gene += bit
            new_genes += new_gene
        self.genes = new_genes

    def _multipoint_crossover_by_gene(self, other, crossover_rate=0.3):
        """Performs multipoint crossover where the crossover points are only
        on different genes, and not the bits in the genes.
        
        At every gene, there is a chance (equal to `crossover_rate`) that
        a new crossover point will be placed. Here is an example of what the
        function does:
        Chromosome A:     AAAA BBBB CCCC DDDD
        Chromosome B:     aaaa bbbb cccc dddd
        Crossover points:     ↕         ↕ 
        After crossover:  AAAA bbbb cccc DDDD

        Args:
            other: The other chromosome that will give its DNA to the
                   offspring.
            crossover_rate: The probability that a new crossover point will be
                            set at any set of genes (default: 0.3).

        Returns:
            This returns a new chromosome which is the "offspring" of this
            chromosome and `other`. This new chromosome contains a genetic
            sequence that is inherited from both "parents".
        """
        longest, shortest = sorted([self._genes, other._genes], key=lambda x: len(x), reverse=True)
        longests_turn = True
        new_genes = []

        # Give the appropriate parent's genes to the offspring
        for i in range(len(longest)):
            if longests_turn:
                new_genes.append(longest[i])
            else:
                # If the shortest has already run out of genes, ignore it
                try:
                    new_genes.append(shortes[i])
                except IndexError:
                    pass

            # Change turn with `crossover_rate` probability
            if random() <= crossover_rate:
                longests_turn = not longests_turn

        return Chromosome(new_genes)

    def get_dna(self):
        """Returns the DNA of the individual chromosome.
        
        This functions returns the DNA of the chromosome in a slightly
        human-readable manner (just a string).
        
        Returns:
            The DNA of the chromosome.
        """
        return ''.join(self._genes)

    def reproduce(self, other, crossover_func, crossover_rate=0.3, mutation_rate=0.001)
        """Performs crossover and then mutation to the new born chromosome.
        
        This function performs crossover and then mutation to a new born
        chromosome that is then returned. Once you have found two chromosomes
        to reproduce with, this is the function to be called to make a new
        chromosome that inherits genes from both its "parents".

        Args:
            other: The other chromosome that will give its DNA to the
                   offspring.
            crossover_func: A string representing the function that will
                            perform the crossover. See the other member
                            functions for a full list of available crossover
                            functions.
            crossover_rate: The probability that a new crossover point will be
                            set at any set of genes (default: 0.3).
            mutation_rate: The probability that any bit of any of the
                           chromosome's genes will flip (default: 0.001). The
                           reason this is a parameter of this function and not
                           a parameter of the constructor of the class, is to
                           allow a varying mutation rate which might be desired
                           in some situations.

        Returns:
            A new chromosome that is the offpsring of `self` and `other`. This
            new offspring also has gone through mutation and so is fully
            prepared to go through a fitness test.
        """
        # Crossover
        if (crossover_func == "multipoint by gene"):
            self._multipoint_crossover_by_gene(other, crossover_rate)
        else:
            print("Unknown crossover function `{0}`. Aborting.".format(crossover_func))
            return

        # Mutate
        self._mutate(mutation_rate)
