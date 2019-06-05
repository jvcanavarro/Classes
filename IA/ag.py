import matplotlib.pyplot as plt
import numpy as np
import struct

# g(x) = x²


def g(x: int) -> int:
    return np.square(x)


# f(x) = x.sin(10pix) + 1
def f(x: float) -> float:
    return x * np.sin(10 * np.pi * x) + 1


def create_population(function: str, pop_size: int) -> float:
    if function == g:
        return np.random.randint(32, size=pop_size)
    elif function == f:
        return np.random.uniform(-1, 2, size=pop_size)


def binary(num):
    return "{0:b}".format(num)


def mutate_chromosome(chromosome: float, rate: int = 50) -> float:

    bin_chromosome = list()

    for base in binary(chromosome):
        if np.random.randint(100) == rate:
            if int(base) == 0:
                bin_chromosome.append(1)
            elif int(base) == 1:
                bin_chromosome.append(0)
        else:
            bin_chromosome.append(int(base))

    int_chromosome = 0
    for bit in bin_chromosome:
        int_chromosome = (int_chromosome << 1) | bit

    return int_chromosome


def mutate_population(population: list) -> list:
    new_population = list()
    for chromosome in population:
        new_population.append(mutate_chromosome(chromosome))
    return new_population


def find_best_case(function: str, population: list = None, pop_size: int = 10, iteration: int = 0, max_value: float = 0) -> float:

    if iteration == 0:
        population = create_population(function, pop_size)

    # Apply on Function
    current_best_result = np.sort(list(map(function, population)))[-1]
    max_value = max(current_best_result, max_value)

    # Stop Conditions:
    # - Exceded number of possible iterations
    # - Maximum possible value found
    if iteration > 9:
        print('Reached last iteration')
        return max_value
    if function == g and max_value == BEST_POSSIBLE_G or function == f and max_value >= BEST_POSSIBLE_F * 0.95:
        print('Expected value found on iteration', iteration)
        return max_value

    iteration += 1
    return find_best_case(function, mutate_population(population), pop_size, iteration, max_value)


def find_both_best_cases():
    return find_best_case(g), find_best_case(f)


BEST_POSSIBLE_G = g(31)
BEST_POSSIBLE_F = f(1.851)

print(find_both_best_cases())
