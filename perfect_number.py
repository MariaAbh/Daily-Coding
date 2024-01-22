#70
counter = 0
i = 0
while True:
    i += 1
    s = str(i)
    nb = sum(map(int, [c for c in s]))
    if nb == 10:
        counter += 1
        print(s, counter)
    if counter == 50:
        break

