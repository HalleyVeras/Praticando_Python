#Conversão de tipo (tipo de conversões)
#O Python oferece duas funções simples para especificar um tipo de dados e resolver esse problema: aqui estão eles: int() e float().

#Seus nomes são de comentários automáticos:

#a função int() usa um argumento (por exemplo, uma string: int(string)) e tenta convertê-lo em um número inteiro; se falhar, o programa inteiro também falhará (há uma solução para essa situação, mas mostraremos isso um pouco mais tarde);
#a função float() usa um argumento (por exemplo, uma string: float(string)) e tenta convertê-la em um flutuante (o resto é o mesmo).

anything = float(input("Digite um número: "))
something = anything ** 2.0
print(anything, "elevado a 2 é", something)
