while True:
    x = float(input())
    
    while x > 10 or x < 0:
        print("nota invalida")
        x = float(input())
    
    y = float(input())
    
    while y > 10 or y < 0:
        print("nota invalida")
        y = float(input())
    
    print(f"media = {(x+y)/2:.2f}")
    
    print("novo calculo (1-sim 2-nao)")
    opcao = int(input())
    
    while opcao < 1 or opcao > 2:
        print("novo calculo (1-sim 2-nao)")
        opcao = int(input())

    if opcao == 1:
        continue
    elif opcao == 2:
        break
    
    