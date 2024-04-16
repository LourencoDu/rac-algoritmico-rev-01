# Eduardo Lourenço da Silva
# Revisão - 01 - 12/04/2024

def ex01():  
  print("Ex.: 1")
  while True: 
    entrada = input("Entre com um número: ")
    if(not entrada.isnumeric()):
      print("Entrada inválida!")
    else:
      break

def ex02():
  print("Ex.: 2")
  nome = input("Nome do usuário: ")
  senha = input("Senha:")
  while (nome == senha):
    print("A senha não pode ser a mesma que o nome do usuário!")
    senha = input("Senha:")
  print("Usuário criado com sucesso!")

def ex03():
  print("Ex.: 3")
  for numero in range(1, 51):
    if(numero % 2 != 0):
      print(numero)

def ex04():
  print("Ex.: 4")
  numero1 = float(input("Entre com o 1º número: "))
  numero2 = float(input("Entre com o 2º número: "))
  numero3 = float(input("Entre com o 3º número: "))

  if(numero1 > numero2 and numero1 > numero3):
    print(f"O maior número é o 1º: {numero1}")
  elif(numero2 > numero1 and numero2 > numero3):
    print(f"O maior número é o 2º: {numero2}")
  elif(numero3 > numero1 and numero3 > numero2):
    print(f"O maior número é o 3º: {numero2}")
  else:
    print("Os números são iguais!")


def ex05():
  print("Ex.: 5")

def ex06():
  print("Ex.: 6")

def ex07():
  print("Ex.: 7")

def ex08():
  print("Ex.: 8")
  

def main():
  opcao = input("Entre com o número do exercício, de 1 a 8: ")
  if(opcao == "1"):
    ex01()
  if(opcao == "2"):
    ex02()
  if(opcao == "3"):
    ex03()
  if(opcao == "4"):
    ex04()
  if(opcao == "5"):
    ex05()
  if(opcao == "6"):
    ex06()
  if(opcao == "7"):
    ex07()
  if(opcao == "8"):
    ex08()
  else:
    print("Opção inválida!")
    main()

main()