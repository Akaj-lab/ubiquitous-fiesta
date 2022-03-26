def samostalniki(s: str):
    out = []
    for i in s:
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            out.append(i)

    return out


def ritem(s: str, rt: str) -> bool:
    r = ""
    for i in f[0]:
        r += 'U' if i.islower() else '-'
    
    return r == rt

with open("vhod.txt", "r") as f:
    f = f.read()
    f = f.split("\n")
    f = [samostalniki(f[i]) for i in range(len(f))]

    rt = ""
    for i in f[0]:
        rt += 'U' if i.islower() else '-'

    for i in f:
        if not ritem(i, rt):
            print("NE")
            break
    

    print("DA", rt, sep="\n")


# najprej iz beselila ločimo samostalnike, ker so to edine črke ki nas zanimajo
# nato ustvarimo "master" ritem, ki ga preverjamo z vsemi ostalimi vrsticami, če je enak potem, vemo, da perem sledi ritmu in ga izpišemo
# če pa med katerokoli vrstico in master ritmom ni ujemanja, vemo, da pesem ne sledi ritmu, zato takrat izpišemo ne in končamo program