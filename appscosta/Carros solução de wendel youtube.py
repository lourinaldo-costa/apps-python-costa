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

veiculos = [ ]
consumo = [ ]
vtpmk = [] # valor total por mil km
carros = [] # lista dicionário nome e custo por mil km - "cpmk"

for i in range(1,4):
    # Coleta e armazenamento de dados
    print("Veículo %i" %i)
    nome = input("Nome: ")
    veiculos.append(nome)
    km = float(input("Km por litro: "))
    consumo.append(km)

    # Variáveis auxiliares e armazenamento
    cpmk =round(float(1000/km*2),2)  # cpmk = custo para mil kilômetros
    vtpmk.append(cpmk)
    nct= {"Nome":nome,"cpmk":cpmk} # É um dicionário cujo nome nct significa: nome e custo total
    carros.append(nct)

print()

# Resultados
print("Relatório Final")

for i in range(3):
    print("%i - %-10s - %6s - %7.1f litros - R$ %7.2f"
          %(i+1,veiculos[i],consumo[i],1000/consumo[i],(1000/consumo[i])*6.5))


# Análise do mais econômico
economico = {"marca": ' ', "consumo": 0}

for carro in carros:
    if carro["cpmk"] < economico["consumo"] or economico["consumo"] == 0:
        economico["consumo"] = carro["cpmk"]
        economico["marca"] = carro["Nome"]
print(f'O veículo mais econômico é o {economico["marca"]}')


