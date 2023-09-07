# (input) é o comando para capturar uma informação e condicionar ela em uma variavel.
# Ex: variavel_1 = input("informe seu nome: ")
# variavel_1 = informação capturada

name = input("Informe o seu nome: ")
age = input("Informe a sua idade: ")
print("Olá " + name +"!" + " Você tem " + age + " anos." )

# O comando (end="...\n") serve para quebra de linha.
print( name, age, end="...\n")

# Já o comando(sep="#") serve para mudar o separador.
print(name, age, sep="#")