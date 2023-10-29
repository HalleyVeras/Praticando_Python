#Mais informações sobre input() e conversão de tipos
#Ter uma equipe composta por três input()-int()-float() abre muitas novas possibilidades.
leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("O comprimento da hipotenusa é", hypo)

#Observe que, no programa que você pode ver no editor, a variável hypo é usada para apenas um objetivo - 
# para salvar o valor calculado entre a execução da linha de código adjacente.

#Como a função print() aceita uma expressão como seu argumento, você pode remover a variável do código.
leg_a = float(input("Insira o comprimento da primeira perna: "))
leg_b = float(input("Insira o comprimento da segunda perna: "))
print("O comprimento da hipotenusa é", (leg_a**2 + leg_b**2) ** .5)