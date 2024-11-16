#Variáveis String

#Pode ser com aspas simples ou duplas
nome = "ada lovelace"
print('ada lovelace')
# apenas em python2 aceita esse comando: print 'ada lovelace'
print(nome)

#Iniciais maiúsculas
print(nome.title())

#tudo maiúscula
print(nome.upper())

#tudo minúscula
nome2 = "ADA LOVELACE"
print(nome2.lower())

#Concatenação com variáveis
primeiro_nome = "ada"
segundo_nome = "lovelace"
nome_inteiro = primeiro_nome + " " + segundo_nome
print(nome_inteiro)

#Concatenação com espaços em brancos
print(primeiro_nome + " " + segundo_nome)
print(primeiro_nome + ' ' + segundo_nome)
print("Olá, " + nome_inteiro.title() + "!")
texto = "Olá, " + nome_inteiro.title() + "!"
print(texto)

#Tabulação
print("Tabubalção:" + "\tPython")
print("Tabubalção:" + "\t" + nome_inteiro.title())

#Quebra de linha
print("Quebra de linha" + "\nLanguages:\nPython\nC\nJavaScript")
print("Quebra de linha" + "\n" + nome_inteiro.title() + "\n" + primeiro_nome + "\n" + segundo_nome)

#Tabulação + Quebra de linha
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#retirar espaço

#lado direito
linguagem_favorita = ' python '
linguagem_favorita = linguagem_favorita.rstrip()
print("#" + linguagem_favorita + "#")
#lado esquerdo
linguagem_favorita = ' python '
linguagem_favorita = linguagem_favorita.lstrip()
print("#" +linguagem_favorita + "#")
#dois lados
linguagem_favorita = ' python '
linguagem_favorita = linguagem_favorita.strip()
print("#" +linguagem_favorita + "#")

#Apóstrofo
#Errado:
#print('One of Python's strengths is its diverse community.')
#Correto
print("One of Python's strengths is its diverse community.")
