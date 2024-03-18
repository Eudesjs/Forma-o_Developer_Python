'''F STRING

As f-strings em Python são uma maneira concisa e elegante de formatar strings.
Elas permitem incorporar expressões Python diretamente dentro de strings,
tornando o código mais legível e fácil de manter.

Como usar f-strings:

Para usar f-strings, basta prefixar uma string literal com a letra "f".
Dentro da string, você pode usar expressões Python entre chaves "{}":
'''
cliente = 'Eudes'
idade = 48
print(f'O nome do Cliente é {cliente}, e ele tem {idade} anos de idade.')
# As Variavel precisam esta entre Colchetes ( {} )

taxa = 2/3
print(taxa)
print(f'O Resultado da taxa é aproximadamente {taxa:.2f}')
# :.2f imprimir o valor com decimal (neste caso 2 casa decimal)