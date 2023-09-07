# Conversão funciona da seguinte forma:
#      variavel_2 = tipo_da_Conversão(variavel_1) 
# Tipos de conversão : int(), str(), float()                               

#Conversão do tipo String para Int:
preco = "10"
valor = int (preco)
x = 5
print(valor - x)

#Conversão do tipo Float para Int:
valor_1 = 7.50
valor_2 = int(valor_1)
valor_3 = "valor 3"
print(valor_2)
     #Perceba que quando se converte de Float para Int, as casas decimais somem.
     

#Comando (type) serve para perguntar para a variavel qual tipo ela é.
print(type(valor_1))
print(type(valor_2))        # O valor_2 está como Int pq passou pela conversão.
print(type(valor_3))