r = 4
c = 8

for r in range(1, r + 1):
    for c in range(1, c + 1):
        if c % 2 == 0:
            print("+", end="")
        else:
            print("*", end="")
    print()