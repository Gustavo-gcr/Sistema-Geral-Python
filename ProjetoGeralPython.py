import random

# Função para ler número por extenso
def numero_por_extenso(num):
    extenso = [
        "zero", "um", "dois", "três", "quatro", 
        "cinco", "seis", "sete", "oito", "nove", 
        "dez", "onze", "doze", "treze", "quatorze", 
        "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"
    ]
    
    if 0 <= num <= 20:
        return extenso[num]
    else:
        return f'ERRO: Número fora do intervalo de 0 a 20. Seu número: {num}'

# Função para simular jogos
def simular_jogos(num):
    jogos = []
    for _ in range(num):
        jogo = [random.randint(0, 60) for _ in range(6)]
        jogos.append(jogo)
    return jogos

# Função para cadastrar pessoas
def cadastrar_pessoas(numPessoas):
    dados = []
    geral = []
    pesadas = []
    leves = []

    for _ in range(numPessoas):
        nome = input('Escreva o nome da pessoa: ')
        peso = float(input('Digite o peso da pessoa: '))
        dados.append([nome, peso])
        geral.append(dados[:])  # Adiciona uma cópia da lista dados a geral

        if peso > 60:
            pesadas.append(dados[:])  # Adiciona uma cópia da lista dados a pesadas
        else:
            leves.append(dados[:])  # Adiciona uma cópia da lista dados a leves
        
        dados.clear()  # Limpa a lista dados para a próxima iteração

    print(f'\nPessoas cadastradas: {numPessoas}')
    print(f'As pessoas mais pesadas e seus pesos são: {pesadas}')
    print(f'Já as pessoas mais leves são: {leves}')

# Lista de produtos
produtos = [
    ('Leite', 22.50), 
    ('Feijão', 31.90),
    ('Macarrão', 99.60),
    ('Chocolate', 31.23),
    ('Doce de Frutas', 98.90),
    ('Cruzeiro BH', 99999999999.61)
]

# Programa Principal
print("\n=== MENU ===")
print("1. Número por extenso")
print("2. Simular jogos")
print("3. Cadastrar pessoas")
print("4. Listar produtos")
print("0. Sair do programa")

opcao = input('Escolha uma opção: ')

while opcao != '0':
    try:
        if opcao == '1':
            num = int(input('Escolha um número para ser escrito por extenso entre 0 e 20: '))
            print(f'Número por extenso: {numero_por_extenso(num)}')
        
        elif opcao == '2':
            num_jogos = int(input('Quantos jogos você deseja simular? '))
            resultados = simular_jogos(num_jogos)
            print(f'No teste de {num_jogos} jogos, esses foram nossos palpites: {resultados}')
        
        elif opcao == '3':
            num_pessoas = int(input('Quantas pessoas você deseja cadastrar? '))
            cadastrar_pessoas(num_pessoas)
        
        elif opcao == '4':
            print('Lista de Produtos:')
            for produto, preco in produtos:
                print(f'{produto}: R${preco:.2f}')
        
        else:
            print('Opção inválida. Escolha novamente.')
            
    except ValueError as erro:
        print(f'ERRO: Valor digitado não é um número inteiro -> {erro}')
    
    print("\n=== MENU ===")
    print("1. Número por extenso")
    print("2. Simular jogos")
    print("3. Cadastrar pessoas")
    print("4. Listar produtos")
    print("0. Sair do programa")
    
    opcao = input('Escolha uma opção: ')

print('Programa encerrado. Obrigado por utilizar!')