n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    soma = 0
    
    for j in range(min(x, y) + 1 , max(x, y)):
        print(j)
        if(j%2 == 1):
            soma += j
    
    print(soma)