from chrome_trex import MultiDinoGame
from genetic_algorithm import load_best_individual, fitness

def main():
    num_dinos = 1  # Apenas uma unidade de Dino
    best_individual = load_best_individual()  # Carrega o melhor indivíduo salvo

    if best_individual is None:
        print("Nenhum indivíduo salvo encontrado.")
        return

    game = MultiDinoGame(num_dinos, 160)  # Inicia o jogo com um único Dino

    score = 0
    while True:
        # Avalia a aptidão do indivíduo no jogo
        score = fitness(best_individual, game)

        # Aqui você pode adicionar a lógica para enviar ações ao Dino, se necessário.
        # Por exemplo, simular saltos ou movimentos com base nas decisões do indivíduo.

        if game.game_over:  # Verifica se o jogo terminou
            print(f"Jogo terminado! Score final: {score}")
            break

    game.close()  # Fecha o jogo ao final

if __name__ == "__main__":
    main()
