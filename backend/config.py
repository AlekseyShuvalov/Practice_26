class GAConfig:
    def __init__(self):
        self.population_size = 100
        self.generations = 500
        self.mutation_chance = 0.1
        self.crossover_chance = 0.8

    def validate(self):
        self.population_size = max(10, min(300, self.population_size))
        self.generations = max(1, min(1000, self.generations))
        self.mutation_chance = max(0.0, min(1.0, self.mutation_chance))
        self.crossover_chance = max(0.0, min(1.0, self.crossover_chance))