i, j = 1, 7
cont = 1

while i < 10:
    print(f"I={i} J={j}")
    if(cont == 3):
        i += 2
        j += 4
        cont = 1
    else:
        j -= 1
        cont += 1