import random
from src.backend.math_functions import StepFunc

class GeneticAlgorithm:
    def __init__(self, polynom, l, r, steps, config):
        self.polynom = polynom
        self.l = l
        self.r = r
        self.steps = steps
        self.config = config
        self.population = []
        self.fitnesses = []
        self.history = []
        self.curr_generation = 0
        self.y_min, self.y_max = polynom.get_bounds(l, r)

    def init_population(self):
        self.population = [[random.uniform(self.y_min, self.y_max) for i in range(self.steps)]
                           for j in range(self.config.population_size)]
        self.curr_generation = 0
        self.history = []
        self.fitnesses = [self.calc_fitness(ind) for ind in self.population]
        self.save_generation_state(self.fitnesses)

    def calc_fitness(self, heights, dots = 300):
        step_func = StepFunc(heights, self.l, self.r)
        step = (self.r - self.l) / dots
        err = 0
        for i in range(dots + 1):
            x = self.l + i * step
            fx = self.polynom.value_at_point(x)
            gx = step_func.value_at_point(x)
            err += abs(fx - gx)
        error = err / (dots + 1)
        return 1 / (1 + error)

    def tournament_selection(self, fitnesses, tournament_size = 3):
        best_id = -100
        best_fitness = -100
        for i in range(tournament_size):
            id = random.randint(0, len(self.population) - 1)
            if fitnesses[id] > best_fitness:
                best_id = id
                best_fitness = fitnesses[id]
        return self.population[best_id][:]

    def crossover(self, first_parent, second_parent): # одноточечное
        if len(first_parent) <= 1: return first_parent[:], second_parent[:]
        c = random.randint(1, len(first_parent) - 1)
        first_child = first_parent[:c] + second_parent[c:]
        second_child = second_parent[:c] + first_parent[c:]
        return first_child, second_child

    def mutation(self, genotype):
        mut_range = (self.y_max - self.y_min) * 0.1
        for i in range(len(genotype)):
            if random.random() < self.config.mutation_chance:
                genotype[i] += random.uniform(-mut_range, mut_range)
                genotype[i] = max(self.y_min - mut_range, min(self.y_max + mut_range, genotype[i]))
        return genotype

    def generation_step(self):
        if self.curr_generation >= self.config.generations: return False
        max_fitness_id = self.fitnesses.index(max(self.fitnesses))

        new_population = []
        new_population.append(self.population[max_fitness_id][:])

        while len(new_population) < self.config.population_size:
            first_parent = self.tournament_selection(self.fitnesses)
            second_parent = self.tournament_selection(self.fitnesses)
            if random.random() < self.config.crossover_chance:
                first_child, second_child = self.crossover(first_parent, second_parent)
            else:
                first_child = first_parent[:]
                second_child = second_parent[:]

            first_child = self.mutation(first_child)
            second_child = self.mutation(second_child)

            new_population.append(first_child)
            if len(new_population) < self.config.population_size: new_population.append(second_child)

        self.population = new_population
        self.curr_generation += 1

        self.fitnesses = [self.calc_fitness(ind) for ind in self.population]
        self.save_generation_state(self.fitnesses)
        return True

    def save_generation_state(self, fitnesses):
        state = {"generation": self.curr_generation, "population": [ind[:] for ind in self.population],
                 "best_genotype": None, "best_fitness": -100, "avg_fitness": -100}
        max_fitness_id = fitnesses.index(max(fitnesses))
        state["best_genotype"] = self.population[max_fitness_id][:]
        state["best_fitness"] = fitnesses[max_fitness_id]
        state["avg_fitness"] = sum(fitnesses) / len(fitnesses)
        self.history.append(state)