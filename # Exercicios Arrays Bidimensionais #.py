# Exercicios bi-arrays #


# 1 - Localização no mapa #

n_colunas = 3
n_linhas = 3
room_desc = []
for i in range(0, n_colunas):
    room_desc.append([])
    for j in range(0, n_linhas):
        room_desc[i].append("Sala x="+str(i)+", y="+str(j))
print(room_desc[1][1])

# 2 - Movimento no mapa # e # 3 - Expação #

x = 1
y = 1
posiçao = (x,y)
histórico = []
direçao = input("Escolhe uma direção para se mover(w,a,s,d)(escreve sair para acabar):")
while direçao != "sair":
    if direçao == "w":
        y = y + 1
        if y > 3:
            y = y - 1
            print("Não existe mais mapa para proseguir")
            direçao = input("Escolhe uma direção para se mover(escreve sair para acabar):")
        else:
            posiçao = (x,y)
            histórico.append(posiçao)
            print("Agora estás na Sala",x ,y)
            direçao = input("Escolhe uma direção para se mover(escreve sair para acabar):")
    elif direçao == "a":
        x = x - 1
        if x < 1:
            x = x + 1
            print("Não existe mais mapa para proseguir")
            direçao = input("Escolhe uma direção para se mover(escreve sair para acabar):")
        else:
            posiçao = (x,y)
            histórico.append(posiçao)
            print("Agora estás na Sala",x ,y)
            direçao = input("Escolhe uma direção para se mover(escreve sair para acabar):")
    elif direçao == "s":
        y = y - 1
        if y < 1:
            y = y + 1
            print("Não existe mais mapa para proseguir")
            direçao = input("Escolhe uma direção para se mover(escreve sair para acabar):")
        else:
            posiçao = (x,y)
            histórico.append(posiçao)
            print("Agora estás na Sala",x ,y)
            direçao = input("Escolhe uma direção para se mover(escreve sair para acabar):")
    elif direçao == "d":
        x = x + 1
        if x > 3:
            x = x - 1
            print("Não existe mais mapa para proseguir")
            direçao = input("Escolhe uma direção para se mover(escreve sair para acabar):")
        else:
            posiçao = (x,y)
            histórico.append(posiçao)
            print("Agora estás na Sala",x ,y)
            direçao = input("Escolhe uma direção para se mover(escreve sair para acabar):")
    else:
        print("Comando inválido")
        direçao = input("Escolhe uma direção para se mover(escreve sair para acabar):")
print("Saiste")
print(histórico)