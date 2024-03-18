'''
A função input() em Python permite que você obtenha entrada do usuário durante a
execução do programa. É uma ferramenta essencial para interagir com o usuário e
coletar dados para processamento.

Como usar a função input():

A função input() é simples de usar. Basta fornecer uma mensagem entre parênteses
para instruir o usuário sobre o que digitar:
'''
nome = input('Informe o seu primeiro nome: ') 
# INPUT Solicita ao usuario a escreve alguma coisa
print(f'Olá, {nome}!') 

nome = input('Informe o seu primeiro nome: ')
massa = float(input('Informe seu peso em Kg: '))
altura = float(input('Informe sua altura em metros na forma decimal: '))
imc = massa / (altura ** 2)

print(f'Ola {nome}! Seu IMC é {imc:.2f}')


''' POSIÇÕES DE CARACTERES NAS STRINGS

Este bloco traz possível soluções para quando queremos saber qual caracter temos
em uma posição (índice) ou sequência de caracteres em um intervalo
'''
# 0    1   2   3   4   5  6  7  8  9 10 11 12 13 (índice)
# -14 -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1 (índice reverso)
# 1º 2º 3º 4º 5º 6º 7º 8º 9º 10º 11º 12º 13º 14º (ordinal)
# d  o  u  g  @  g  m  a  i   l   .   c   o   m
email = 'eudsjs@gmail.com'
print(email[4])
print(email[:]) # imprimir um intervalo de todos os caracteres da string email
print(email[0:4]) # selecionando o intervalo a partir do índice 0 até o índice 3
print(email[2:]) # seleciona o intervalo a partir do índice 2 até o final
print(email[:5]) # seleciona o intervalo de todos os caracteres até o de índice 4
print(email[0:5:2]) # seleciona último caracter de uma sequência
'''
resumo do fatiamento de strings
nome_variavel[indice de começo : índice de parada : de quanto em quanto]
nome_variavel[início : fim : passo]
'''

# CONTAR A QUANTIDADE DE CARACTERES EM UMA SEQUENÇIA
email = 'eudsjs@gmail.com'
print(len(email)) # LEN - mostra a quantidade que tem um objeto
qtde = len(email)
print(qtde)

cpf = 14378132400
print(type(cpf))
cpf = str(cpf) # Transforma um int em Str
print(type(cpf))

''' OPERDOR IN - verifica se um determinado valor esta presente
em uma sequencia retorna Verdadeiro ou Falso (true , false).
'''
email = 'eudsjs@gmail.com'
print('u' in email)

''' OPERADOR NOT IN - Verifica se um valor nao esta presente em uma
sequencia. Retorna Verdadeiro ou Falso (true , false)

'''
emial = 'eudsjs@gmail.com'
print('u' not in email)

# METODO CAPITALIZE() CONVERTE UM MAIUSCULA APENAS A PRIMEIRA LETRA DE
# DE UMA STRING.
nome = 'eudes'
print(nome)
nome = nome.capitalize()
print(nome)

# METODO TITLE(), SERVE PARA DEIXAR A PRIMEIRA LETRA DE CADA PALAVRA
# MAIUSCULA
nome = 'eudes jose da silva'
print(nome)
nome = nome.capitaliza() # Deixar a primeira letra do primeiro nome Maiuscula
print(nome)
nome = nome.title() #deixa a primeira letra de todas as palavras maiuscula
print(nome)

# METODO UPPER() DEIXA TODAS AS LETRAS MAIUSCULAS
nome = 'eudes josé da silva'
print(nome)
nome = nome.upper()
print(nome)

# METODO COUNT() CONTA QUANTAS VEZES UM DETERMINADO CARACTER APARECE EM UMA 
# STRING.
email = 'eudsjs@gmail.com'
email.count('@')

# METODO FIND() MOSTRA A POSIÇÃO DE UM DETERMINADO CARACTERES
# CASO APAREÇA MAIS DE UMA VEZ, ELE POR PADRÃO MOSTRARÁ A PRIMEIRA
email = 'eudsjs@gmail.com'
email.find('u') # retorna true ou false

# METODO STARTSWITH() VERIFICA SE UMA STRING COMEÇA COM UM DETERMINADO
# CARACTER OU SEQUENCIA DE CARACTERES
email = 'eudsjs@gmail.com'
email.startswith('eud') #retorna true ou false

# METODO ENDSWITH() VERIFICA SE UMA STRING TERMINA COM UM DETERMINADO
# CARACTER OU SEQUENCIA DE CARACTERES
email = 'eudsjs@gmail.com'
email.endswith('.com')

# METODO ISNUMERIC() VERIFICA SE O CONTEUDO DE UMA STRING É OU NAO NUMERICO
cpf = '04378132400'
cpf.isnumeric()

# METODO ISALPHA() VERIFICA SE O CONTEUDO DE UMA STRING É OU NAO LETRAS
nome = 'Eudes Silva'
nome.isalpha()

# METODO ISALNUM() VERIFICA SE O CONTEUDO DE UMA STRING É OU NAO COMBINAÇÃO
# DE LETRAS E NUMEROS.
nome = 'Eudes'
nome.isalnum()

# METODO STRIP() REMOVE ESPAÇOS INDESEJADOS NO COMEÇO E/OU FINAL DA STRING
nome = ' Eudes'
print(len(nome))
nome = nome.strip()
print(len(nome))

# METODO REPLACE SUBSTITUI UM CARACTER POR OUTRO.
preco = 'R$ 10.50'
preco = preco.replace('.' , ',')
print(preco)

# METODO SPLIT() DIVIDE UMA STRING EM DUAS OU MAIS PARTES POR MEIO
# DE UM SEPARADOR
nome = 'Eudes José da Silva'
nome = nome.split()
print(nome)

date = '12/05/2023'
dia_mes_ano = date.split('/')
print(dia_mes_ano)



