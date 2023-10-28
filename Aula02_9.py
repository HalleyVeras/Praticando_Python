#Lista de prioridades
#1	**
#2	+, - (observação: operadores unários localizados ao lado direito do operador de potência se vinculam mais fortemente))	unário
#3	*, /, //, %
#4	+, -

#Ambos os operadores (* e %) têm a mesma prioridade, portanto, o resultado pode ser adivinhado apenas 
#quando você sabe a direção da encadernação. O que você acha? Qual é o resultado?
print(2 * 3 % 5)

#Operadores e parênteses
#De acordo com as regras aritméticas, subexpressões entre parênteses são sempre calculadas primeiro.

#Você pode usar quantos parênteses precisar, e eles geralmente são usados para melhorar a legibilidade de uma expressão,
#mesmo que não alterem a ordem das operações.
print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)