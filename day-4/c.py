r = 5
c = 8

for r in range(1, r + 1):
    for c in range(1, c + 1):
        if r % 2 == 0:
            print("X", end="")
        else:
            print(c, end="")
    print()