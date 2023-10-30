#Operadores de string
#É hora de voltar para esses dois operadores aritméticos: + e *.

#Queremos mostrar que eles têm uma segunda função. Eles são capazes de fazer algo mais do que apenas adicionar e multiplicar.
fnam = input("Posso ter seu primeiro nome, por favor? ")
lnam = input("Posso ter seu sobrenome, por favor? ")
print("Obrigado!.")
print("\nSeu nome é " + fnam + " " + lnam + ".")
#Nota: usar + para concatenar strings permite que você construa a saída de uma maneira mais precisa do que com uma função print()
#pura, mesmo se enriquecida com os argumentos de palavra-chave end= e sep=.
##############################################

#Replicação
#O sinal * (asterisco), quando aplicado a uma string e um número
#(ou um número e uma string, pois permanece comutativo nessa posição) se torna um operador de replicação:

#Um número menor ou igual a zero produz uma string vazia.

#Este simples programa "desenha" um retângulo, fazendo uso de um antigo operador (+) em um novo papel:
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
