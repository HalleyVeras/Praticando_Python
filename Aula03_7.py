#Conversões de tipo mais uma vez concluídas
#str()
#Você já sabe como usar as funções int() e float() para converter uma string em um número.

#O triângulo de ângulo direito novamente
leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
print("O comprimento da hipotenusa é " + str((leg_a**2 + leg_b**2) ** .5))