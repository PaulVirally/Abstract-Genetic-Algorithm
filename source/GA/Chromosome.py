import random

class Chromosome:

    def __init__(self, genes):
        """Creates a new Chromosome.
        
        Arguments:
            genes {[str]} -- The genes of the chromosome are a list of strings with each string being the encoding of one gene.
        """
        self.genes = genes

    def mutate(self, mutation_rate):
        """Mutates the genes of the Chromosome at a rate of `mutation_rate`.
        
        You may want to write your own `mutate` function if your gene encoding is different than what is normally assumed.

        Arguments:
            mutation_rate {float} -- The rate of mutation.
        """
        new_genes = []
        for gene in self.genes:
            # Assume binary encoding in an int format
            if isinstance(gene, int):
                to_int = True
                gene = bin(gene)[2:] # We now have a string of 1s and 0s

            # Assume binary encoding in a string of 1s and 0s
            new_gene = ''
            for bit in gene:
                if random.random() < mutation_rate:
                    new_gene += '1' if bit == '0' else '0' # Flip the bit
                else:
                    new_gene += '1' if bit == '1' else '0' # Preserve the bit
                        
            if to_int: # If we had an int before, make sure we have an int after
                new_gene = int(gene, 2)
                            
            new_genes.append(new_gene)

        self.genes = new_gene