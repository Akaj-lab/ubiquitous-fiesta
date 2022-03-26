# vhod dobimo iz datoteke vhod1.txt
# m in n pa dobimo prek standardnega vhoda od vsake takoj odštejemo 1 ker računalniki začnejo štet z 0 ne 1
m = int(input("Stolpci")) - 1
n = int(input("Vrstice")) - 1

def strtolist(s: str):
    li = []
    for i in s:
        li.append(i)
    return li


def najdistonoge(a):
    stonoge = []
    i = 0
    while i < n:
        j = 0
        while j < m:
            if a[i][j] == '#':
                k = j 
                while a[i][j] == '#':
                    j += 1
                if a[i][j+1] == ">":
                    dire = 1
                else:
                    dire = -1
                stonoge.append((i, k, j, dire))
            j += 1
        i += 1

    return stonoge


with open("vhod1.txt", "r") as f:
    f = f.read()
    f = f.split("\n")
    f = [strtolist(j) for j in f] 

    ok = 0
    niok = 0

    # najdi stonoge
    stonoge = najdistonoge(f)
    vse = len(stonoge)

    #preged simetričnosti
    for i in stonoge:
        a, b, c, points = i
        for j in range(c):
            if (f[a - 1][b + c] == "|" and f[a + 1][b + c] == "|") or (f[a - 1][b + c] == "/" and f[a + 1][b + c] == "\\") or (f[a - 1][b + c] == "\\" and f[a + 1][b + c] == "/"):
                continue #stonoga je simetrična
            else:
                niok += 1
                for neki in range(c):
                    f[a][b + neki] = '*'
                break # pojdi na naslednjo stonogo ta ni v redu ker ni ok damo # v * in v naslednjem koraku še enkrat najdemo stonoge, vendar tokrat nsamo tiste ki so še mogoče ok

    stonoge = najdistonoge(f)
    # pregled ostalih lastonsti
    for i in stonoge:
        a, b, c, points = i,
        if f[a - 1][b - 1] == '\\' and points == -1:
            continue # ok zaenkrat
        elif f[a - 1][b + c + 1] == '\\' and points == 1:
            continue # zaenkrat ok
        else:
            niok += 1
            break # ta stonoga ni ok

    ok = vse - niok



    
