# Um programa que lê uma sequência de números
# e conta quantos números são pares e quantos são ímpares.
# O programa termina quando zero é digitado.

odd_numbers = 0
even_numbers = 0

# Leia o primeiro número.
number = int(input("Digite um número ou digite 0 para parar: "))

# 0 termina a execução.
while number != 0:
    # Verifique se o número é ímpar.
    if number % 2 == 1:
        # Aumente o contador odd_numbers.
        odd_numbers += 1
    else:
        # Aumente o contador even_numbers.
        even_numbers += 1
    # Leia o número seguinte.
    number = int(input("Digite um número ou digite 0 para parar: "))

# Imprimir resultados.
print("Números ímpares contam:", odd_numbers)
print("Números pares contam:", even_numbers)