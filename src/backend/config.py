class GAConfig:
    def __init__(self):
        self.population_size = 100
        self.generations = 500
        self.tournament_size = 3
        self.mutation_chance = 0.1
        self.crossover_rate = 0.8

    def validate(self):
        self.population_size = max(10, min(1000, self.population_size))
        self.generations = max(1, min(5000, self.generations))
        self.tournament_size = max(2, min(10, self.tournament_size))
        self.mutation_chance = max(0.0, min(1.0, self.mutation_chance))
        self.crossover_rate = max(0.0, min(1.0, self.crossover_rate))