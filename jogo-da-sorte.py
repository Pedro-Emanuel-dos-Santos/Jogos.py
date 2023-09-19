import random

def jogo_de_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")
    
    while True:
        try:
            palpite = int(input("Digite o seu palpite: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue
        
        tentativas += 1
        
        if palpite < numero_secreto:
            print("Tente um número maior.")
        elif palpite > numero_secreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    jogo_de_adivinhacao()
