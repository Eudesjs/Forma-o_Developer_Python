# Fundamentos em Python
'''VARIAVEIS E TIPOS DE DADOS EM PYTHON
Em ython variaveis sao utilizadas para armazenar valores na memoria do
computador. para criar uma variavel, voce precisa usar um nome e um valor.

1 - VARIAVEIS
    - Deve começar com uma letra ou sublinhados (_)
    - Pode conter letras, numeros ou sublinhados
    - Nao pode conter palavras chaves reservadas do Python
    - Para atribuir um valor a uma variavel utilize o operador
    de atribuição ( = ).
    EXEMPLO:
'''
nome = 'Eudes Silva' #Variavel mais Valor
print(nome) #Imprime na tela o Valor da Variavel Nome.
print(type(nome)) #(type) mostrar o Tipo da Variavel nome.
                # Tipo String (str)

idade = 41 #Variavel Idade, Valor 41
print(idade) 
print(type(idade)) # Tipo de Variavel Inteiro (int)

altura = 1.70 # Na linguagem Python o ( . ) é um separador decimal
print(altura)
print(type(altura)) # TIpo da Variavel Ponto Flutuante (FLoat)

idade1 = 41
idade2 = 45
print(idade1 > idade2) 
print(type(idade1 > idade2)) # Tipo de Variavel Booleno (bool)

print('Ola Mundo!')
# FIM
