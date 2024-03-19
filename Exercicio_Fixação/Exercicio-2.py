'''
Suponha que o preço de capa de um livro seja R$ 24,95, 
mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00
para o primeiro exemplar e 75 centavos para cada exemplar adicional.
 Qual é o custo total de atacado para 60 cópias?
'''
import math

# Preço de capa do livro
preco_capa = 24.95

# Desconto aplicado às livrarias (40%)
desconto = 0.40

# Custo de transporte para o primeiro exemplar
custo_primeiro_exemplar = 3.00

# Custo de transporte para cada exemplar adicional
custo_exemplar_adicional = 0.75

# Quantidade de cópias
quantidade_copias = 60

# Calculando o preço com desconto
preco_desconto = preco_capa * (1 - desconto)

# Calculando o custo de transporte para todas as cópias
custo_transporte = custo_primeiro_exemplar + custo_exemplar_adicional * (quantidade_copias - 1)

# Calculando o custo total de atacado
custo_total_atacado = preco_desconto * quantidade_copias + custo_transporte

# Exibindo o resultado
print("O custo total de atacado para 60 cópias é R$ {:.2f}".format(custo_total_atacado))
