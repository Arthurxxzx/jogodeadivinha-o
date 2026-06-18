print("*********************************")
print("Bem vindo ao jogo de adivinhação")
print("*********************************")

numero_secreto = 67

chute = input("Digite o seu número: ")
print("Você digitou: ",chute )

chutenumerico = int(chute)
if(numero_secreto == chutenumerico ):
   print("Você acertou!")
else:
   print("Você errou!")
       

print("Fim do jogo")
