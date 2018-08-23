
print("****************************************")
print("Olá, Bem-vindo(a) ao jodo de advinhação!")
print("****************************************")

numero_secreto = 42

chute = int(input("Digite um número: "))

print("você digitou ", chute)

if (numero_secreto == chute):
    print("Parabéns! Você acertou o número!!")
else:
    print("Sinto muito, você errou o número.. Tente novamente!")