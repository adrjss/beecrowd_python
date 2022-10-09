while True:
    x, y = map(int, input().split())
    
    if (x <= 0 or y <= 0):
        break
    else:
        soma = 0
        for i in range(min(x,y), max(x,y)+1):
            print(i, end=' ')
            soma += i
        print(f"Sum={soma}")