#A função input() - operações proibidas
# Testando uma mensagem TypeError.

anything = input("Digite um número: ")
something = anything ** 2.0
print(anything, "elevado a 2 é", something)

#A última linha da frase explica tudo - você tentou aplicar o operador ** a 'str' (string) acompanhado de 'float'.

#Isso é proibido.

#Isso deve ser óbvio - você pode prever o valor de "ser ou não ser" elevado à potência de 2?

#Nós não podemos. Python também não.

#Já caímos em um impasse? Há uma solução para esse problema? Claro que sim.