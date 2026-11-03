r = 8
c = 8

for r in range(1, r + 1):
    for c in range(1, c + 1):
        if(r % 2 == 0 and c % 2 == 0) or (r % 2 > 0 and c % 2 > 0):
            print("X", end="")
        else:
            print("O", end="")
    print()