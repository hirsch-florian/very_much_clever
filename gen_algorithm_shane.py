# -*- coding: utf-8 -*-
"""
Created on 2019-07-26 11:17

@author: sharding
"""

import random
from typing import List, Tuple

OPTIMAL = "Hello python guild"
DNA_SIZE = len(OPTIMAL)
POPULATION_SIZE = 100
GENERATIONS = 50_000
# GENERATIONS = 1000


def weighted_choice(items: List[Tuple[str, float]]) -> str:
    """ chooses a random element from the items list with a probability associated with its
        weight """
    total_weight = sum(item[1] for item in items)
    n = random.uniform(0, total_weight)
    for item, weight in items:
        if weight > n:
            return item
        n -= weight
    return item


def random_charachter() -> chr:
    """ return a random character between asci 32 and 126 (letters, numbers, symbols and spaces """
    return chr(int(random.randrange(32, 126, 1)))


def random_population() -> List:
    """ generate a random population. each element is of length dna_size and consists of random
        characters """
    pop = []
    for _ in range(POPULATION_SIZE):
        dna = ""
        for c in range(DNA_SIZE):
            dna += random_charachter()
        pop.append(dna)
    return pop


def calculate_fitness(dna: str) -> float:
    """ define a fitness function as being the distance a string is from the optimal. make minimum
        fitness 1 to avoid possible division by zero later """
    # make minimum fitness 1 to avoid possible division by zero later
    fitness = 1
    for c in range(DNA_SIZE):
        fitness += abs(ord(dna[c]) - ord(OPTIMAL[c]))
    return 1 / fitness


def random_mutate(dna: str) -> str:
    """ randomly mutate a character to ensure genepool diversity and reduce risk of getting stuck
        in local minima/maxima """
    result = ""
    for c in range(DNA_SIZE):
        if random.randrange(0, 100, 1) == 1:
            result += random_charachter()
        else:
            result += dna[c]
    return result


def crossover(mother: str, father: str) -> Tuple[str, str]:
    """ mate a mother and father gene to create two child genes """
    position = random.randrange(0, DNA_SIZE, 1)
    return mother[:position] + father[position:], father[:position] + mother[position:]


def main():
    """ main function """
    population = random_population()
    weighted_population = []
    target_fitness = calculate_fitness(OPTIMAL)
    # calculate fitness and weights
    for dna in population:
        fitness = calculate_fitness(dna)
        weighted_population.append((dna, fitness))

    for gen in range(GENERATIONS):

        # clear population as we are going to evolve and readd the results
        population.clear()
        # read to population
        for _ in range(int(POPULATION_SIZE / 2)):
            dna_1 = weighted_choice(weighted_population)
            dna_2 = weighted_choice(weighted_population)

            dna_1 = random_mutate(dna_1)
            dna_2 = random_mutate(dna_2)

            dna_1, dna_2 = crossover(dna_1, dna_2)
            population.extend([dna_1, dna_2])
            # print(len(population))
        weighted_population.clear()
        #
        fittest = ("", 0.0)
        for dna in population:
            fitness = calculate_fitness(dna)
            weighted_population.append((dna, fitness))

            if fitness > fittest[1]:
                fittest = (dna, fitness)
                if fitness == target_fitness:
                    print(f"Target '{fittest[0]}' reached in generations {gen}")
                    return
        if gen % 10 == 0:
            print(f"Fittest candidate after {gen} generations = {fittest[0]}")


if __name__ == "__main__":
    main()