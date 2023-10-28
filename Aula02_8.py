#Operadores e suas prioridades
#Então, se você sabe que * tem uma prioridade mais alta que +, o cálculo do resultado final deve ser óbvio.
print(2 + 3 * 5)
###############################
#da esquerda para a direita: primeiro 9 % 6 dá 3, e então 3 % 2 dá 1;
#da direita para a esquerda: primeiro 6 % 2 dá 0 e depois 9 % 0 causa um erro fatal.
print(9 % 6 % 2)
###############################
#Os dois resultados possíveis são:

#2 ** 2 → 4; 4 ** 3 → 64
#2 ** 3 → 8; 2 ** 8 → 256
#O resultado mostra claramente que o operador de exponenciação usa a associação do lado direito.
print(2 ** 2 ** 3)
####################
print(-3 ** 2) 
print(-2 ** 3) 
print(-(3 ** 2))