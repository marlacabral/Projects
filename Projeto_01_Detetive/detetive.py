
import random

print('Detetive')

inicio = input("Para começar aperte [X] ").strip().upper()[0]
print(' ')
if inicio == 'X':
  print('Bem-vindo ao Detetive !')
else:
  print(f"Ops ! Tente novamente.")

bemVindo = input('Aperte [X]').strip().upper()[0]
if bemVindo == 'X':
  print("Iniciando o jogo.")
  print("-"* 17)
else:
  print("Tente novamente.")


print(" ")
caso1 = 'Sofia de 34 anos, foi encontrada em seu quarto com marcas de estrangulamento.\nResponda com [S/N] para provar sua inocência.'
caso2 = 'Lucas de 29 anos, foi localizado caído em sua mesa de jantar, com evidências de envenenamento.\nResponda com [S/N] para provar sua inocência.'
caso3 = 'Michele de 19 anos, foi encontrada em sua piscina, evidências indicam assassinato por afogamento.\nResponda com [S/N] para provar sua inocência.'

casos = [caso1, caso2, caso3]
sorteio = random.choice(casos)


if bemVindo == 'X':
  print(sorteio)
else:
  print("Tente novamente.")

print(" ")

perguntas = str(input("Aperte [X] para continuar: ")).strip().upper()[0]
if perguntas == 'X':
  p1 = print("Você telefonou para a vítima?")
  r1 = str(input('[S/N]: ')).strip().upper()[0]
    

  p2 = print("Você esteve no local do crime?")
  r2 = str(input('[S/N]: ')).strip().upper()[0]

  p3 = print("Você mora perto da vítima?")
  r3 = str(input('[S/N]: ')).strip().upper()[0]

  p4 = print("Você devia para a vítima?")
  r4 = str(input('[S/N]: ')).strip().upper()[0]

  p5 = print("Você já trabalhou com a vítima?")
  r5 = str(input('[S/N]: ')).strip().upper()[0]
else:
  print(f'Ops ! Tente novamente.{perguntas}')

if r1 == 'S' and r2 == 'S' and r3 == 'S' and r4 =='S' and r5 == 'S':
  print("assassino !")
  print("Você foi pego em flagante e foi condenado à 20 anos de prisão.")

elif r1 == 'N' and r2 == 'S' and r3 == 'S' and r4 =='S' and r5 == 'S':
  print("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")
elif r1 == 'S' and r2 == 'N' and r3 == 'S' and r4 =='S' and r5 == 'S':
  print("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")
elif r1 == 'S' and r2 == 'S' and r3 == 'N' and r4 =='S' and r5 == 'S':
  tprint("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")
elif r1 == 'S' and r2 == 'S' and r3 == 'S' and r4 =='N' and r5 == 'S':
  print("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")
elif r1 == 'S' and r2 == 'S' and r3 == 'S' and r4 =='S' and r5 == 'N':
  print("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")

elif r1 == 'N' and r2 == 'N' and r3 == 'S' and r4 =='S' and r5 == 'S':
  print("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")
elif r1 == 'S' and r2 == 'S' and r3 == 'S' and r4 =='N' and r5 == 'N':
  print("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")
elif r1 == 'N' and r2 == 'S' and r3 == 'N' and r4 =='S' and r5 == 'S':
  print("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")
elif r1 == 'S' and r2 == 'S' and r3 == 'N' and r4 =='S' and r5 == 'N':
  print("cumplice")
  print("Você foi julgado com cúplice e pagará a fiança de 12 anos de prisão.")

elif r1 == 'S' and r2 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r1 == 'S' and r3 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r1 == 'S' and r4 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r1 == 'S' and r5 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r2 == 'S' and r3 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r2 == 'S' and r4 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r2 == 'S' and r5 == "S":
  tprint("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r3 == 'S' and r4 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r3 == 'S' and r5 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")
elif r4 == 'S' and r5 == "S":
  print("suspeito")
  print("Você é suspeito de assassinato e qualquer coisa dita, pode ser usada contra você.")

elif r1 == 'N' and r2 == 'N' and r3 == 'N' and r4 =='N' and r5 == 'N':
  print("inocente")
  print("O interrogatório prosseguirá com os demais suspeitos.")
else:
  print(" Comando inválido! Tente novamente.")

print(" ")
print("FIM")