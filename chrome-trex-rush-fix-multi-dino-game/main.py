from chrome_trex import MultiDinoGame
from genetic_algorithm import initialize_population, next_generation, fitness, save_best_individual, load_best_individual

def main():
    # Parâmetros do Algoritmo Genético
    POP_SIZE = 50
    NUM_GENERATIONS = 5
    num_dinos = 50

    # Carrega o melhor indivíduo da última execução, se existir
    best_individual = load_best_individual()

    # Inicializa a população
    population = initialize_population(POP_SIZE, num_dinos)
    if best_individual:
        population[0] = best_individual  # Substitui o primeiro indivíduo pelo melhor carregado

    game = MultiDinoGame(num_dinos, 0)  # Ajuste para o número de dinossauros

    # Executa o algoritmo genético
    for generation in range(NUM_GENERATIONS):
        print(f"Generation {generation+1}/{NUM_GENERATIONS}")

        # Avalia a aptidão de cada indivíduo
        scores = [fitness(individual, game) for individual in population]

        # Emparelha os indivíduos com seus scores
        population_scores = list(zip(population, scores))

        # Seleciona o melhor indivíduo e seu score
        best_individual, best_score = max(population_scores, key=lambda pair: pair[1])

        print(f"Best score in generation {generation+1}: {best_score}")

        # Seleciona os melhores indivíduos e cria a próxima geração
        population = next_generation(population, game)

        # Salva o melhor indivíduo da geração
        save_best_individual(best_individual)

    # Fecha o jogo quando terminar
    game.close()

if __name__ == "__main__":
    main()
