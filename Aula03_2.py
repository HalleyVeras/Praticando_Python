#A função input()
print("Conta-me qualquer coisa...")
anything = input()
print("Hum...", anything, "... Realmente?")

#O programa solicita que o usuário insira alguns dados do console
#(provavelmente usando um teclado, embora também seja possível inserir dados usando voz ou imagem);
#a função input() é invocada sem argumentos (essa é a maneira mais simples de usar a função); a função 
#mudará o console para o modo de entrada; você verá um cursor piscando e poderá inserir algumas teclas, 
#finalizando pressionando a tecla Enter; todos os dados inseridos serão enviados ao seu programa através do resultado da função;
#nota: você precisa atribuir o resultado a uma variável; isso é crucial - perder esta etapa fará com que os dados inseridos sejam perdidos;
#em seguida, usamos a função print() para exibir os dados que obtemos, com algumas observações adicionais.
#####################################################################################
#A função input() com um argumento
anything = input("Conta-me qualquer coisa...")
print("Hum...", anything, "...Realmente?")
#a função input() é invocada com um argumento ‒ é uma string contendo uma mensagem;
#a mensagem será exibida no console antes que o usuário tenha a oportunidade de digitar qualquer coisa;
#input() fará seu trabalho.
#Essa variante da invocação input() simplifica o código e o torna mais claro.