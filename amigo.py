import random
import os
import time

def limpar_tela():
    # Limpa o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

# 1. Lista com os seus 16 participantes
participantes = [
    "Aparecida", "Paulo", "Luciana", "Valcirlei", "Sandra",
    "Isabela", "Ney", "Elaine", "Rosilene", "Leandro",
    "Andrey", "Willamy", "Luis", "Luan", "Luisa", "Alexandre"
]

def realizar_sorteio_secreto(lista_nomes):
    embaralhados = lista_nomes.copy()
    random.shuffle(embaralhados)

    # Cria o dicionário secreto de resultados
    sorteio = {}
    for i in range(len(embaralhados)):
        quem_tirou = embaralhados[i]
        quem_foi_tirado = embaralhados[(i + 1) % len(embaralhados)]
        sorteio[quem_tirou] = quem_foi_tirado

    # Sistema de inputs para entrega individual
    while len(sorteio) > 0:
        limpar_tela()
        print("=== SISTEMA DE AMIGO SECRETO ===")
        print(f"Faltam {len(sorteio)} pessoas verem seus pares.\n")
        
        # MOSTRA OS PARTICIPANTES CADASTRADOS EM TODA TURNA
        print("Participantes cadastrados:")
        print(", ".join(lista_nomes))
        print("-" * 50)  # Linha separadora para organizar o visual
        
        nome = input("Digite o SEU nome exatamente como acima (ou 'sair'): ").strip()
        
        if nome.lower() == 'sair':
            break
            
        if nome in sorteio:
            resultado = sorteio[nome]
            print(f"\n {nome}, você tirou: {resultado} ")
            
            # Remove da lista para ninguém consultar o mesmo nome duas vezes
            del sorteio[nome]
            input("\nAperte ENTER quando terminar de ler para apagar a tela...")
        else:
            print("\n Nome não encontrado ou você já viu seu amigo! Tente novamente.")
            time.sleep(2.5)
            
    limpar_tela()
    print("Sorteio concluído com sucesso!")

# Executa o programa
realizar_sorteio_secreto(participantes)
