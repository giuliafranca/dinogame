import random
import numpy as np
from chrome_trex import MultiDinoGame, ACTION_UP, ACTION_FORWARD, ACTION_DOWN, action_list

# Função para avaliar a aptidão de um indivíduo
def fitness(individual, game):
    game.reset()
    while not game.game_over:
        state = game.get_state()
        actions = action_list(state)
        game.step(actions)
    return max(game.get_scores())

# Inicializa a população com indivíduos aleatórios
def initialize_population(pop_size, num_dinos):
    population = []
    for _ in range(pop_size):
        # Cada indivíduo é uma lista de ações para cada dinossauro
        individual = [random.choice([ACTION_UP, ACTION_FORWARD, ACTION_DOWN]) for _ in range(num_dinos)]
        population.append(individual)
    return population

# Seleção por torneio
def tournament_selection(population, scores, tournament_size):
    selected = []
    for _ in range(len(population)):
        tournament = random.sample(list(zip(population, scores)), tournament_size)
        winner = max(tournament, key=lambda x: x[1])[0]
        selected.append(winner)
    return selected

# Cross-over entre dois indivíduos
def crossover(parent1, parent2, crossover_rate):
    if random.random() < crossover_rate:
        point = random.randint(1, len(parent1) - 1)
        return parent1[:point] + parent2[point:]
    else:
        return parent1

# Mutação de um indivíduo
def mutate(individual, mutation_rate):
    return [random.choice([ACTION_UP, ACTION_FORWARD, ACTION_DOWN]) if random.random() < mutation_rate else action
            for action in individual]

# Modificar a função next_generation para incluir elitismo
def next_generation(population, game, tournament_size=3, crossover_rate=0.7, mutation_rate=0.01, elite_size=1):
    # Avalia a aptidão de cada indivíduo
    scores = [fitness(individual, game) for individual in population]
    
    # Ordena a população com base nos scores
    sorted_population = [x for _, x in sorted(zip(scores, population), key=lambda pair: pair[0], reverse=True)]
    
    # Preserva a elite (os melhores indivíduos)
    new_population = sorted_population[:elite_size]
    
    # Seleção por torneio
    selected = tournament_selection(sorted_population, scores, tournament_size)
    
    # Cria nova população por cruzamento e mutação
    while len(new_population) < len(population):
        parent1 = random.choice(selected)
        parent2 = random.choice(selected)
        child1 = crossover(parent1, parent2, crossover_rate)
        child2 = crossover(parent2, parent1, crossover_rate)
        new_population.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])
    
    # Retorna a nova população, truncada se exceder o tamanho da população original
    return new_population[:len(population)]

import pickle

# Função para salvar o melhor indivíduo em um arquivo
def save_best_individual(best_individual, filename="best_dino.pkl"):
    with open(filename, 'wb') as f:
        pickle.dump(best_individual, f)

# Função para carregar o melhor indivíduo de um arquivo
def load_best_individual(filename="best_dino.pkl"):
    try:
        with open(filename, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

