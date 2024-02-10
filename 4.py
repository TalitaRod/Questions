#SP = 67836.43
#RJ = 36678.66
#MG = 29229.88
#ES = 27165.48
#Outros = 19849.53

def percentual (estado, total):
    percentual = (estado / total) * 100
    return percentual

vet = [67836.43, 36678.66, 29229.88, 27165.48, 19849.53]
soma = 0

for i in vet:
    soma += i
    i += 1

for j in vet:
    per = percentual(j, soma)
    print(per)