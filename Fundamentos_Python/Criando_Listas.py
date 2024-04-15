'''
Lista em Python podem armazenar de maneira sequencial,
qualquer tipo de objeto. podemos criar listas utilizando,
o construtor list, a função range ou colocando valores separados,
por virgula dentro de colchetes. listas são objetos mutáveis,
portanto podemos alterar seus valores após a criação.
EX.
'''
#frutas = ["Laranja", "Maca", "Uva"] # Forma mais comum
#print(frutas)
#frutas = [] # Posso declarar uma lista vazia
#print(frutas)
#letras = list("Python") # Uma Variavel recebendo o Construtor List
#print(letras)
#numeros = list(range(10)) # criar um elemento da funcao range
#print(numeros)
#carros = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
'''
A forma mais comum para percorrer os dados de uma lista é
utilizando o comando for.
'''
#for carro in carros:
#    print(carro)

'''
As vezes é necessario saber qual o indice do objeto dentro do
laço for. para isso podemos usar a função enumerate.
'''
#for indice, carro in enumerate(carros):
#    print(f"{indice}: {carro}")

'''
A compreensão de lista oferece uma sintaxe mais curta quando você,
deseja: Criar uma nova lista com base nos valores de uma lista,
existente (filtro) ou gerar uma nova lista aplicando alguma modificação,
nos elementos de uma lista existente.
'''
#VERSÃO 1
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    print(pares)

#VERSÃO 2
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)
#VERSAO 3

quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado)