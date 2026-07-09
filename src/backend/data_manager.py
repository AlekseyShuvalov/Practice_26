import json
import random
from math_functions import Polynom
from config import GAConfig


class DataManager:
    def generate_random_polynom(self, max_degree=8):
        degree = random.randint(1, max_degree)
        coefficients = [random.randint(-5, 5)
                        for _ in range(degree + 1)]
        return Polynom(coefficients)

    def generate_random_task(self):
        polynom = self.generate_random_polynom()
        l = random.randint(-10, 0)
        r = random.randint(1, 10)
        return {
            'polynom': polynom.cfs,
            'interval': [l, r],
            'steps': random.randint(10, 35)
        }

    def save_to_file(self, filename, task_data, config=None):
        data = {
            'polynom': task_data['polynom'],
            'interval': task_data['interval'],
            'steps': task_data['steps']
        }

        if config is not None:
            data['ga_config'] = {
                'population_size': config.population_size,
                'generations': config.generations,
                'tournament_size': config.tournament_size,
                'mutation_chance': config.mutation_chance,
                'crossover_rate': config.crossover_rate
            }

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.validate_task_data(data)

        task_data = {
            'polynom': data['polynom'],
            'interval': data['interval'],
            'steps': data['steps']
        }

        config = None
        if 'ga_config' in data:
            config = GAConfig()
            config.population_size = data['ga_config']['population_size']
            config.generations = data['ga_config']['generations']
            config.tournament_size = data['ga_config']['tournament_size']
            config.mutation_chance = data['ga_config']['mutation_chance']
            config.crossover_rate = data['ga_config']['crossover_rate']
            config.validate()

        return task_data, config

    def validate_task_data(self, data):   # Валидация данных
        if 'polynom' not in data:
            raise ValueError("Отсутствует поле 'polynom'")
        if 'interval' not in data:
            raise ValueError("Отсутствует поле 'interval'")
        if 'steps' not in data:
            raise ValueError("Отсутствует поле 'steps'")

        if not isinstance(data['polynom'], list):
            raise ValueError("'polynom' должен быть списком")
        if len(data['polynom']) > 9:
            raise ValueError("Степень полинома не должна превышать 8")

        if not isinstance(data['interval'], list) or len(data['interval']) != 2:
            raise ValueError("'interval' должен быть списком из 2 элементов")
        if data['interval'][0] >= data['interval'][1]:
            raise ValueError("Начало интервала должно быть меньше конца")

        if not isinstance(data['steps'], int) or data['steps'] < 1:
            raise ValueError("'steps' должен быть положительным целым числом")