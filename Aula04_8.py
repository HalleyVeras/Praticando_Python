#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#    "Telefonou para a vítima?"
#    "Esteve no local do crime?"
#    "Mora perto da vítima?"
#    "Devia para a vítima?"
#    "Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

# Função para fazer uma pergunta e obter uma resposta do usuário (S ou N)
def fazer_pergunta(pergunta):
    resposta = input(pergunta + " (S/N): ").strip().lower()
    while resposta not in ['s', 'n']:
        resposta = input("Por favor, responda com S (sim) ou N (não): ").strip().lower()
    return resposta

# Inicializa um contador para rastrear as respostas afirmativas
contador = 0

# Fazer as 5 perguntas
pergunta1 = fazer_pergunta("Telefonou para a vítima?")
if pergunta1 == "s":
    contador += 1

pergunta2 = fazer_pergunta("Esteve no local do crime?")
if pergunta2 == "s":
    contador += 1

pergunta3 = fazer_pergunta("Mora perto da vítima?")
if pergunta3 == "s":
    contador += 1

pergunta4 = fazer_pergunta("Devia para a vítima?")
if pergunta4 == "s":
    contador += 1

pergunta5 = fazer_pergunta("Já trabalhou com a vítima?")
if pergunta5 == "s":
    contador += 1

# Classifica a participação da pessoa no crime com base nas respostas
if contador == 5:
    classificacao = "Assassino"
elif contador >= 3:
    classificacao = "Cúmplice"
elif contador >= 2:
    classificacao = "Suspeita"
else:
    classificacao = "Inocente"

# Exibir a classificação
print(f"Classificação: {classificacao}")
