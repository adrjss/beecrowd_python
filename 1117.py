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
    break
    
    