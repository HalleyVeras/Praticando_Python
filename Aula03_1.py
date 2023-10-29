#Como usar uma variável

var = 1
account_balance = 1000.0
client_name = 'John Doe'
print(var, account_balance, client_name)
print(var)

#No entanto, você não pode usar uma variável que não existe
#(em outras palavras, uma variável que não recebeu um valor).
#var = 1
#print(Var)

#Você pode usar a função print() e combinar texto e variáveis 
#usando o operador + para gerar sequências e variáveis. Por exemplo:
var = "3.8.5"
print("Versão Python: " + var)

#Como atribuir um novo valor a uma variável já existente
var = 1
print(var)
var = var + 1
print(var)

#A primeira linha do trecho cria uma nova variável chamada var e atribui 1 a ela.

#A instrução diz: atribua um valor de 1 a uma variável denominada var.

#Podemos dizer mais curto: atribua 1 ao var.

#Alguns preferem ler uma declaração como: var se torna 1.

#A terceira linha atribui a mesma variável com o novo valor retirado da própria variável, somada com 1. Vendo um registro como esse, um matemático provavelmente protestaria - nenhum valor pode ser igual a si mesmo mais um. Isso é uma contradição. Mas Python trata o sinal = não como igual a, mas como atribuir um valor a.

#Então, como você lê esse registro no programa?

#Pegue o valor atual da variável var, adicione 1 e armazene o resultado na variável var.

#Com efeito, o valor da variável var tem sido incrementado por um, o que não tem nada a ver com a comparação da variável com qualquer valor.
############
####################
# Bem, primeiro, o var variável é criada e recebe o valor 100.
#Em seguida, a mesma variável recebe um novo valor: o resultado da adição de 200 a 300, que é 500.
var = 100
var = 200 + 300
print(var)
