i, j = 0, 1

while i <= 2:
    if(i % 1 == 0 or i > 1.9):
        print(f"I={i:.0f} J={j:.0f}")
    else:
        print(f"I={i:.1f} J={j:.1f}")
    j += 1
    if(j >= (i + 4)):
        i += 0.2
        j -= 2.8