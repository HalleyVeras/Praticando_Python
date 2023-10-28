#Python como uma calculadora
print(2+2)
print (3-2)
print (10/2)
print(5*10)
##################################
#quando os dois ** argumentos são inteiros, o resultado também é um número inteiro;
print(2 ** 3)
#Quando pelo menos um argumento ** é um float, o resultado também é um float.
print(2 ** 3.)
#Quando pelo menos um argumento ** é um float, o resultado também é um float.
print(2. ** 3)
#Quando pelo menos um argumento ** é um float, o resultado também é um float.
print(2. ** 3.)

###############################################
print(2 * 3)
#Quando pelo menos um argumento * é um float, o resultado também é um float.
print(2 * 3.)
#Quando pelo menos um argumento * é um float, o resultado também é um float.
print(2. * 3)
#Quando pelo menos um argumento * é um float, o resultado também é um float.
print(2. * 3.)

############################################################################
#O resultado produzido pelo operador de divisão é sempre um float, 
#independentemente de parecer ou não ser um flutuante à primeira vista:
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.)

#Divisão de número inteiro (divisão arredondada)
#Um sinal // (barra dupla) é um operador de divisão inteira. Difere do padrão / operador em dois detalhes:

#seu resultado não possui a parte fracionária ‒ está ausente (para inteiros), ou é sempre igual a zero 
#(para flutuantes); isso significa que os resultados são sempre arredondados;
#ele está de acordo com a regra integer vs. float.
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)
#Como você pode ver, a divisão de inteiro por inteiro dá um resultado inteiro. 
#Todos os outros casos produzem floats.

print(-6 // 4)
print(6. // -4)

################################################################################################
#Restante (módulo)
print(14 % 4)
#14 // 4 dá 3 → este é o quociente inteiro;
#3 * 4 dá 12 → como resultado da multiplicação de quociente e divisor;
#14 - 12 dá 2 → este é o restante.

print(12 % 4.5)

#não 3 mas 3.0. A regra ainda funciona:

#12 // 4.5 dá 2.0,
#2.0 * 4.5 dá 9.0,
#12 - 9.0 dá 3.0.
