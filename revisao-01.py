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
  numero1 = int(input("Entre com o 1º número inteiro: "))
  numero2 = int(input("Entre com o 2º número inteiro: "))

  if(numero1 == numero2):
    print("Os números não podem ser iguais!")
  else:
    menor = min(numero1, numero2)
    maior = max(numero1, numero2)
    print(f"Números no intervalo de {menor} e {maior}:")

    for numero in range(menor + 1, maior):
      print(numero)

def ex06():
  print("Ex.: 6")
  numero1 = int(input("Entre com o 1º número inteiro: "))
  numero2 = int(input("Entre com o 2º número inteiro: "))

  if(numero1 == numero2):
    print("Os números não podem ser iguais!")
  else:
    menor = min(numero1, numero2)
    maior = max(numero1, numero2)
    soma = 0
    print(f"Números no intervalo de {menor} e {maior}:")

    for numero in range(menor + 1, maior):
      print(numero)
      soma += numero
    print(f"Soma dos números: {soma}")

def ex07():
  print("Ex.: 7")
  votosA = 0
  votosB = 0
  votosC = 0
  qtdEleitores = int(input("Entre com a quantidade de eleitores: "))
  for eleitor in range(1, qtdEleitores + 1):
    print(f"Eleitor Nº{eleitor}")
    voto = input("Em qual condidato deseja votar, A, B ou C? ").upper()
    while(voto != "A" and voto != "B" and voto != "C"):
      voto = input(f"O candidato {voto} não existe, escolha outro: ")
    if(voto == "A"):
      votosA += 1
    elif(voto == "B"):
      votosB += 1
    else:
      votosC += 1
  print(f"Candidato A: {votosA} voto(s)")
  print(f"Candidato B: {votosB} voto(s)")
  print(f"Candidato C: {votosC} voto(s)")
    

def ex08():
  print("Ex.: 8")
  nome = input("Entre com o nome: ")
  while(len(nome) <= 3):
    print("O nome deve ter mais que 3 caracteres!")
    nome = input("Entre com o nome: ")

  idade = int(input("Entre com a idade: "))
  while(idade < 0 or idade > 150):
    print("A idade deve estar entre 0 e 150!")
    idade = int(input("Entre com a idade: "))

  salario = float(input("Entre com o salário: "))
  while(salario <= 0):
    print("O salário deve ser maior que 0 (zero)!")
    salario = float(input("Entre com o salário: "))

  sexo = input("Entre com o sexo: ").lower()
  while(not (sexo in {"f", "m"})):
    sexo = input(f"{sexo} não é uma opção válida! escolha 'f' ou 'm':")

  estado_civil = input("Entre com o estado civil: ").lower()
  while(not (estado_civil in {"s", "c", "v", "d"})):
    estado_civil = input(f"{estado_civil} não é uma opção válida! escolha 's', 'c', 'v' ou 'd':")

  print("Todas as validações passaram!")
  print(f"Nome: {nome}")
  print(f"Idade: {idade}")
  print(f"Salário: {salario}")
  print(f"Sexo: {sexo}")
  print(f"Estado Civil: {estado_civil}")
  
  

def main():
  opcao = input("Entre com o número do exercício, de 1 a 8: ")
  if(opcao == "1"):
    ex01()
  elif(opcao == "2"):
    ex02()
  elif(opcao == "3"):
    ex03()
  elif(opcao == "4"):
    ex04()
  elif(opcao == "5"):
    ex05()
  elif(opcao == "6"):
    ex06()
  elif(opcao == "7"):
    ex07()
  elif(opcao == "8"):
    ex08()
  else:
    print("Opção inválida!")

  main()

main()