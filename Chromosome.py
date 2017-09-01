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

    def mutate(self, mutation_rate=0.001):
        """Mutates the choromosome to add some randomness to the evolution
        process.
        
        This will flip any bit in the chromosome's genes with a probability
        equal to `mutattion_rate`.
        
        Args:
            mutation_rate: The probability that any bit of any of the
            chromosome's genes will flip (default: 0.001). The reason this is 
            a parameter of this function and not a paramter of the constructor
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
            other: The other chromosome that will give its DNA to the offspring
            crossover_rate: The probability that a new crossover point will be
                            set at any set of genes (default: 0.3)

        Returns:
            This returns a new chromosome which is the "offspring" of this
            chromosome and `other`. This new chromosome contains a genetic
            sequence that is inherited from both "parents"
        """
        longest, shortest = sorted([self._genes, other._genes],
                key=lambda x: len(x), reverse=True)

