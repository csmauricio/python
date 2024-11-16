#Listas
print("Listas")

#lista vazia
print("\nLista vazia")
jogos = []
print(jogos)

print("\nCriando listas")
jogos = ['D&D', 'God Of War', 'Spider-Man', 'E-Fotball']
jogos = ["D&D", "God Of War", "Spider-Man", "E-Fotball"]
print(['D&D', 'God Of War', 'Spider-Man', 'E-Fotball'])
print(jogos)

print("\nListando por parâmetro")
print(jogos[0])
print(jogos[1])
print(jogos[2])
print(jogos[3])

print("\nListando primeira maiúscula")
print(jogos[3].title())
print("\nListando tudo maiúscula")
print(jogos[3].upper())
print("\nListando tudo minúsculo")
print(jogos[3].lower())

print("\nListando concatenando")
print(jogos[0] + " " + jogos[3]) 
print("\nListando concatenando com funções maúsculas e minúsculas")
print(jogos[3].lower() + " " + jogos[3].upper()) 

#último elemento da lista
print("\nListando último elemento da lista")
print(jogos[-1])

#alterar lista
print("\nAlterando lista")
jogos = ['D&D', 'God Of War', 'Spider-Man', 'E-Fotball']
print(jogos)
jogos[2] = "Red Dead Redemption"
jogos[2] = 'Red Dead Redemption'
print(jogos)

#Inserir no final
print("\nInsereindo no final")
jogos = ['D&D', 'God Of War', 'Spider-Man', 'E-Fotball']
print(jogos)
jogos.append('Red Dead Redemption')
jogos.append("Red Dead Redemption2")
print(jogos)

#Inserir em qualquer posição (cudiade que depois que inserir uma nova psoição, as demais modificam)
print("\nInsereindo em qualquer posição")
jogos = ['D&D', 'God Of War', 'Spider-Man', 'E-Fotball']
print(jogos)
jogos.insert(0,'Red Dead Redemption')
jogos.insert(4,"Red Dead Redemption2")
print(jogos)

#limpando lista
print("\nlimpando lista")
jogos = []
print(jogos)

#limpar um registro específico (cudiade que depois que inserir uma nova psoição, as demais modificam)
print("\nLimpar parâmetro específico")
jogos = ['D&D', 'God Of War', 'Spider-Man', 'E-Fotball']
print(jogos)
del jogos[3]
print(jogos)

#Removendo pelo método pop (retira sempre o último item da lista e guarda para outro uso depois, ou para indicar qual foi o último item inserido na lista
print("\nRemovendo pelo método pop (retira sempre o último item da lista e guarda para outro uso depois, ou para indicar qual foi o último item inserido na lista")
jogos = ['D&D', 'God Of War', 'Spider-Man', 'E-Fotball']
print(jogos)
popped_jogos = jogos.pop()
print(popped_jogos)

#removendo item da lista pelo valor (apenas o primeiro que aparecer na lista, se tiver mais valores iguais, tem que fazer um loop passando item a item 
print("\nRemovendo item da lista pelo valor (apenas o primeiro que aparecer na lista, se tiver mais valores iguais, tem que fazer um loop passando item a item")
jogos = ['D&D', 'God Of War', 'Spider-Man', 'E-Fotball']
print(jogos)
jogos.remove("God Of War")
print(jogos)

print("\nRemovendo item da lista pelo valor e guardando o valor")
jogos = ['D&D', 'God Of War', 'Spider-Man', 'E-Fotball']
print(jogos)
remover = "God Of War"
jogos.remove(remover)
print(jogos)
print(remover)

#Ordenando listas
print("\nOrdenando listas")
jogos = ['D&D', 'God Of War', 'Spider-Man', 'E-Fotball']
print(jogos)
jogos.sort()
print(jogos)

print("\nOrdenando listas reversa")
jogos = ['D&D', 'God Of War', 'Spider-Man', 'E-Fotball']
print(jogos)
jogos.sort(reverse=True)
print(jogos)

print("\nOrdenando listas mas mantendo a original")
jogos = ['D&D', 'God Of War', 'Spider-Man', 'E-Fotball']
print(jogos)
print(sorted(jogos))
print(jogos)

print("\nOrdenando em ordem inversa")
jogos = ['D&D', 'God Of War', 'Spider-Man', 'E-Fotball']
print(jogos)
jogos.reverse()
print(jogos)

print("\nTamanho da lista (começa em 1)")
jogos = ['D&D', 'God Of War', 'Spider-Man', 'E-Fotball']
print(jogos)
tamanho = len(jogos)
print(tamanho)
