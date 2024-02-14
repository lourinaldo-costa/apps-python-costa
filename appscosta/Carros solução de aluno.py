# Minha solução dos veículos ficou:
"""
Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo
de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo
desses carros, isto é, quantos quilômetros cada um desses carros faz com um
litro de combustível. Calcule e mostre:

a.	O modelo do carro mais econômico;
b.	Quantos litros de combustível cada um dos carros cadastrados consome
para percorrer uma distância de 1000 quilômetros e quanto isto custará,
considerando que a gasolina custe R$ 6,25 o litro.

Abaixo segue uma tela de exemplo. A disposição das informações deve ser o mais
próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada
execução do programa.

Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: vectra
Km por litro: 9
Veículo 5
Nome: peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.
"""

carros = [] # É uma lista de dicionários

for c in range(3):
    novoCarro = {"marca": input('Marca do carro: '), "km": float(input('Quilômetros rodados por litro.'))}

    novoCarro["consumo"] = round(1000 / novoCarro["km"], 2)  # https://acervolima.com/funcao-round-em-python
    carros.append(novoCarro)

for pos, carro in enumerate(carros): # https://pythonhelp.wordpress.com/2012/01/05/a-funcao-enumerate/
    print(f'{pos + 1} - {carro["marca"]:15}-{str(carro["km"]):>10} - {str(carro["consumo"]) + " Litros":>15} - R$ {carro["consumo"] * 6}')
    # 15 foi estabelecido como o número mínimo de caracteres. 6 é o valor de R$ 6,00/litro.
    # {str(carro["km"]):>10} Definido que só aceita mais que 10 Km/litro 


economico = {"marca": ' ', "consumo": 0}

for carro in carros:
    if carro["consumo"] < economico["consumo"] or economico["consumo"] == 0:
        economico["consumo"] = carro["consumo"]
        economico["marca"] = carro["marca"]
print(f'O carro mais econômico é o {economico["marca"]}')
print()
print(carros)
print(economico.items())

# Função enumarate()

"""
l = ['hello', 'world', 'hi', 'earth']
for i, word in enumerate(l):
    print (i, word)
"""
# Funções literais formatadas https://docs.python.org/pt-br/3/tutorial/inputoutput.html
"""
7.1.1. Strings literais formatadas
Strings literais formatadas (também chamadas f-strings, para abreviar) permite que se inclua o valor de expressões
Python dentro de uma string, prefixando-a com f ou F e escrevendo expressões na forma {expression}.

Um especificador opcional de formato pode ser incluído após a expressão. Isso permite maior controle sobre como
o valor é formatado. O exemplo a seguir arredonda pi para três casas decimais:

>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
Passando um inteiro após o ':' fará com que o campo tenha um número mínimo de caracteres de largura. Isso é útil
para alinhar colunas.
"""

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items(): # Aqui table.items() converte numa lista
    print(f'{name:10} ==> {phone:10d}')

"""
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
"""























