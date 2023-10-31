#Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. 
#Dica: utilize o operador módulo (resto da divisão): %

numero = int(input('Digite um inteiro: '))

if numero%2 :
    print("Ímpar")
else:
    print("Par")