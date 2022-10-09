while True:
    x, y = map(int, input().split())
    
    if x == 0 or y == 0:
        break
    
    if x > 0:
        print("primeiro") if y > 0 else print("quarto")
    else:
        print("segundo") if y > 0 else print("terceiro")
    