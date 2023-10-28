#Se quiser dar um nome a uma variável, você deve seguir algumas regras estritas:

#o nome da variável deve ser composto de letras maiúsculas ou minúsculas, dígitos e o caractere _ (sublinhado)
#o nome da variável deve começar com uma letra;
#o caractere de sublinhado é uma letra;
#as letras maiúsculas e minúsculas são tratadas como diferentes (um pouco diferente do que no mundo real -
# Alice e ALICE são os mesmos nomes, mas em Python são dois nomes de variáveis diferentes e, consequentemente, duas variáveis diferentes);
#o nome da variável não deve ser nenhuma das palavras reservadas do Python (as palavras-chave - explicaremos mais sobre isso em breve).

# Correct:
#MyVariable             
#i
#l
#t34
#Exchange_Rate
#counter
#days_to_christmas
#TheNameIsTooLongAndHardlyReadable
#_
#Adiós_Señora
#sûr_la_mer
#Einbahnstraße
#переменная.

#E agora, alguns nomes incorretos:

#10t (não começa com uma letra)
#!important (não começa com uma letra)
#exchange rate (contém um espaço).

var=1
print(var)

#Palavras-chave
#['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 
# 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
# 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']