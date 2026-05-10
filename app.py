nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

with open("dados.txt", "w") as arquivo:
    arquivo.write(f"Nome: {nome}\n")
    arquivo.write(f"Idade: {idade}")

print("Dados salvos com sucesso!")
