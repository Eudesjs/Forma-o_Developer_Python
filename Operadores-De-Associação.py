'''
Os operadores de associação in e not in em Python permitem verificar se um
elemento está presente ou não em uma coleção, como listas, tuplas, dicionários e
strings. São ferramentas úteis para filtrar dados e realizar comparações em seus
programas. Assim como os aoperadores de comparação eles retornam
Verdadeiro (True) ou Falso (False)
'''
# OPERADOR ( in )
nome = 'Eudes'
print('E' in nome) # E esta presente na Variavel NOME ('Eudes')

# OPERADOR ( not in )
nome = 'Eudes'
print('E' not in nome) # E nao esta presente na Variavel NOME ('Eudes')

''' OPERADORES LOGICOS ( AND, OR, NOT )

Os operadores lógicos em Python permitem combinar expressões booleanas
(True ou False) para formar novas expressões booleanas. São ferramentas
essenciais para tomar decisões e realizar comparações complexas em seus
programas. São eles:

E (and): Retorna True se ambas as expressões forem True.
Exemplo: x > 0 and y < 10.

Ou (or): Retorna True se pelo menos uma das expressões for True.
Exemplo: x == 0 or y == 10.

Não (not): Inverte o valor da expressão.
Exemplo: not (x > 0).
'''
# OPERADOR ( AND = E ) RETORNA VERDADEIRO SE TODAS AS CONDIÇÕES FOREM VERDADEIRAS
a = 3
b = 4
c = 5
print(a < b and b < c) # Retorna true ambos sao verdades
print(a < b and b > c) # Retorna false uma nao é verdade

# OPERADOR ( OR = OU ) RETORNA VERDADEIRO SE PELO MENOS UMA DAS CONDIÇÕES FOR VERDADEIRO
a = 3
b = 4
c = 5
print(a < b or b < c ) # Retorna Verdadeiro
print(a < b or b > c ) # Retorna Verdadeiro
print(a > b or a > c ) # Retorna Falso

# O OPERADOR (NOT = NAO ) INVERTE O RESULTADO DE VERDADEIRO PARA FALSO E DE FALSO PARA VERDADEIRO.
a = 3
b = 4
c = 5
print(not( a > b )) # Retorna verdadeiro
print(not( a < b )) # Retorna Falso