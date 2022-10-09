inter = 0
gremio = 0
empate = 0
cont = 1

def pontuar(x, y):
    if x > y:
        global inter
        inter += 1
    elif x < y:
        global gremio
        gremio += 1
    else:
        global empate
        empate += 1

while True:
    x, y = map(int, input().split())
        
    pontuar(x, y)
    
    opcao = 0
    while opcao < 1 or opcao > 2:
        print("Novo grenal (1-sim 2-nao)")
        opcao = int(input())
        
    if opcao == 1:
        cont += 1
        
    if opcao == 2:
        print(f"{cont} grenais")
        print(f"Inter:{inter}")
        print(f"Gremio:{gremio}")
        print(f"Empates:{empate}")
        if inter > gremio:
            print("Inter venceu mais")
        elif gremio > inter:
            print("Gremio venceu mais")
        else:
            print("Nao houve vencedor")
            
        break
        
    
        
