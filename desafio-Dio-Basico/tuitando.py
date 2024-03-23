#######DESAFIO#######
'''
O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. 
Conferir se um texto vai caber em um tuíte é sua tarefa.
'''

'''
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída.
'''
t = input()

if len(t) <= 140:
    print("tweet")
else:
    print("MUTE")

'''
TODO Ler a variável de entrada e verificar se ela possui mais ou menos que 140 caracteres.
    Se for maior imprima "MUTE" e se for igual ou menor imprima "TWEET".
'''