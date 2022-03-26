def BeriStevec() -> list[int]:
    return

sez0 = BeriStevec()
possible = sez0.copy()
while len(possible) > 1: # dokler seznam možnih številk vsebuje več kot 1 element, ponavljamo, nato vrnemo vrednost 
    possible.clear()
    sez1 = BeriStevec()
    for i in sez0:
        if i - 1 in sez1:
            possible.append(i - 1)

    sez0 = possible.copy()


print(possible[0])


# program v seznam possible najprej zapiše vse možne števke funkcije BeriStevec nato pa jih počasi odstranjuje, ko le te ne morejo več biti možne številke