n = int(input())

cobaias = {
    "R": 0,
    "S": 0,
    "C": 0
}

for i in range (n):
    cobaia = input().split()
    cobaias[cobaia[1].upper()] += int(cobaia[0])
    
print(f"Total: {sum(cobaias.values())} cobaias")
print(f"Total de coelhos: {cobaias['C']}")
print(f"Total de ratos: {cobaias['R']}")
print(f"Total de sapos: {cobaias['S']}")
print(f"Percentual de coelhos: {round(cobaias['C']/sum(cobaias.values())*100, 2):.2f} %")
print(f"Percentual de ratos: {round(cobaias['R']/sum(cobaias.values())*100, 2):.2f} %")
print(f"Percentual de sapos: {round(cobaias['S']/sum(cobaias.values())*100, 2):.2f} %")