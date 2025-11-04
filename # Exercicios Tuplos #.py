# Exercicios Tuplos #

# 1 - Herói #

herói = ("Kaisen","67","420","21")
nome, nivel, HealthPoints, experiencia = herói
print("O herói",nome,"está no nível",nivel,"com",HealthPoints,"HP e",experiencia,"XP.")
print("----------------------------------------------------------")

# 2 - coordenadas #

spawn_point = (0,0,0)
x, y, z = spawn_point
print("A coordenada x é",x)
print("A coordenada y é",y)
print("A coordenada z é",z)
print("----------------------------------------------------------")

# 3 - NPC #

npc = ("Morshu","40","Lamp Oil","Rope","Bombs")
nome, idade, item1, item2, item3 = npc
print(nome, "vende:", item1 + ",", item2,"e", item3)
print("----------------------------------------------------------")

# 4 - moedas #

moedas = (5, 10, 2)
ouro, prata, bronze = moedas
valor_moeda = (5, 3, 1)
valorouro, valorprata, valorbronze = valor_moeda
print("Existem",ouro,"moedas de ouro,",prata,"moedas de prata e",bronze,"moedas de bronze")
print("Existem",int(ouro)+int(prata)+int(bronze),"moedas no total")
print("Cada meoda de ouro tem o valor de",valorouro,", cada moeda de prata tem o valor de",valorprata,"e cada moeda de bronze tem o valor de",valorbronze)
print("O valor total de todas as moedas é",int(ouro)*int(valorouro)+int(prata)*int(valorprata)+int(bronze)*int(valorbronze))
print("----------------------------------------------------------")

# 5 - scores #

scores = ("Ana","Bruno","Carla","David","Eva")
aluno1, aluno2, aluno3, aluno4, aluno5 = scores
lista1 = (aluno1,aluno2)
lista2 = (aluno3,aluno4,aluno5)
print(lista1)
print(lista2)