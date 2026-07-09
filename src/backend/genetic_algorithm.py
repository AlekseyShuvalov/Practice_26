import random
from math_functions import *

# Генетический алгоритм

def calc_fitness(heights, cfs, l, r, dots = 300):
    err = 0
    step = (r - l) / dots
    for i in range(dots + 1):
        x = l + i * step
        fx = poly_value_at_point(cfs, x)
        gx = step_func_value_at_point(heights, l, r, x)
        err += abs(fx - gx)
    error = err / (dots + 1)
    return 1 / (1 + error)

def tournament_selection(population, fitnesses, tournament_size = 3):
    best_id = -100
    best_fitness = -100
    for i in range(tournament_size):
        id = random.randint(0, len(population) - 1)
        if fitnesses[id] > best_fitness:
            best_id = id
            best_fitness = fitnesses[id]
    return population[best_id]

def crossover(first_parent, second_parent): # одноточечное
    if len(first_parent) == 1: return first_parent[:], second_parent[:]
    c = random.randint(1, len(first_parent) - 1)
    first_child = first_parent[:c] + second_parent[c:]
    second_child = second_parent[:c] + first_parent[c:]
    return first_child, second_child

def mutation(genotype, mutation_chance, y_min, y_max):
    mut_range = (y_max - y_min) * 0.1
    for i in range(len(genotype)):
        if random.random() < mutation_chance:
            genotype[i] += random.uniform(-mut_range, mut_range)
            genotype[i] = max(y_min - mut_range, min(y_max + mut_range, genotype[i]))
    return genotype

def genetic_algorithm(cfs, l, r, steps, population_size, generations, mutation_chance):
    y_min, y_max = bounds_of_polynom(cfs, l, r)
    population = [[random.uniform(y_min, y_max) for i in range(steps)] for j in range(population_size)]
    best_genotype = None
    best_fitness = -100
    max_fitnesses = []
    avg_fitnesses = []
    for generation in range(generations):
        fitnesses = [calc_fitness(ind, cfs, l, r) for ind in population]
        max_fitness_id = fitnesses.index(max(fitnesses))
        curr_max_fitness = fitnesses[max_fitness_id]
        curr_avg_fitness = sum(fitnesses) / len(fitnesses)
        max_fitnesses.append(curr_max_fitness)
        avg_fitnesses.append(curr_avg_fitness)
        if curr_max_fitness > best_fitness:
            best_fitness = curr_max_fitness
            best_genotype = population[max_fitness_id][:]

        new_population = []
        new_population.append(best_genotype[:])
        while len(new_population) < population_size:
            first_parent = tournament_selection(population, fitnesses)
            second_parent = tournament_selection(population, fitnesses)
            first_child, second_child = crossover(first_parent, second_parent)

            first_child = mutation(first_child, mutation_chance, y_min, y_max)
            second_child = mutation(second_child, mutation_chance, y_min, y_max)

            new_population.append(first_child)
            if len(new_population) < population_size: new_population.append(second_child)
        population = new_population

    return best_genotype, max_fitnesses, avg_fitnesses