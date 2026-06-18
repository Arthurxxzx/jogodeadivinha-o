print("*********************************")
print("Bem vindo ao jogo de adivinhação")
print("*********************************")

numero_secreto = 67

chute = input("Digite o seu número: ")
print("Você digitou: ",chute )

chutenumerico = int(chute)

acertou = chutenumerico == numero_secreto
maior = chutenumerico > numero_secreto
menor = chutenumerico < numero_secreto



if(acertou):
   print("Você acertou!")
else:
   if(maior):
       print("Você errou! O seu chute foi maior que o número secreto.")
   elif(menor):
       print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim do jogo")
