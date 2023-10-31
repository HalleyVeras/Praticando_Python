#Pedimos o primeiro número ao usuário, e armazenamos na variável 'num1'.
#Em seguida, pedimos o segundo e colocamos na variável 'num2'.

#Agora vamos aos testes!
#Primeiro, testamos se o primeiro é maior que o segundo:  num1 > num2 
#Se for verdade, exibimos que num1 é o maior e pronto.

#Pode ser que sejam iguais!
#Então, precisamos fazer outro teste IF dentro desse ELSE (estruturas aninhadas!) perguntando se são iguais.
num1=int( input('Digite o primeiro numero: ') )
num2=int( input('Digite o segundo numero: ') )

if num1 > num2 :
    print('O primeiro, %d, é maior' %num1)
else:
    if num1 == num2 :
        print('Os números são iguais')
    else:
        print('O segundo, %d, é maior' %num2)