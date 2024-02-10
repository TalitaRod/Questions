import xml.etree.ElementTree as ET
from statistics import mean


def lerXml(vetor = []):
    tree = ET.parse('dados.xml')
    root = tree.getroot()
    print(root.tag)

    for i in root.findall('row'):
        valor = i.find('valor').text 
        vetor.append(valor)

faturamento = []
total = 0
diasFaturamento = 0
superior = 0


lerXml (faturamento)
for j in faturamento:
    print(j)

#O menor valor de faturamento ocorrido em um dia do mês;
menor = min(faturamento)
print(f'O menor valor de faturamento é: {menor}')

#O maior valor de faturamento ocorrido em um dia do mês;
maior = max(faturamento)
print(f'O maior valor de faturamento é: {maior}')

#Número de dias no mês em que o valor de faturamento diário foi superior à média mensal;
for dia in faturamento:
    if dia != '0.0000':
        diasFaturamento += 1
        dia = float(dia)
        total += dia
        dia += 1

mediaMensal = total / diasFaturamento

for dia in faturamento:
    dia = float(dia)
    if dia > mediaMensal:
        superior += 1

print(f'Dias no mês em que o valor de faturamento diário foi superior à média mensal: {mediaMensal: .2f} foram {superior}.')



