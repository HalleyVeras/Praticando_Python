secret_number = 777  # O número secreto escolhido pelo mágico
print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")
while True:
    try:
        user_number = int(input("Adivinhe o número secreto: "))
        if user_number == secret_number:
            print("Muito bem, trouxa! Você está livre agora.")
            break  # Sai do loop se o número for adivinhado corretamente
        else:
            print("Ha ha! Você está preso no meu loop!")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
