# loop skozi senzorje snežink, ko zazna prešteje vse aktivirane žice nato gleda samo srednjo, in, kot ta ni več aktivna se vrne na začetek programa
def Senzor(n: int) -> bool:
    return
    # zazna ali je žica aktivirana



# zazamo da se je snežinka dotaknila žice
def zaznajsnezinko(i: int):
    if Senzor(i):
        return i # vrnemo i, ker je to zagotovo ena izmed žic, ki se je je dotaknila snežinka, od tu naprej gledamo samo dokler je ta žica aktivirana
    elif i == 100:
        return False
    else:
        return zaznajsnezinko(i + 1)

def zadnjazica(i: int):
    if Senzor(i):
        return i
    else:
        return zadnjazica(i - 1)

# pojavi se problem, ker lahko snežinka pade tudi med tem ko je program nekje na sredi zanke zaznajsnezinko, 
# zato ni nujno, da je število, ko ga vrne zaznajsnezinko enko 1. žici ki se jo je dotaknila snežinka
# problem rešimo, tako da še enkrat pregledamo vse žice, tokrat pa bomo zagotovo našli 1.

# ko imamo 1. žico najdemo še zadnjo

# vrnemo razliko
def prestejzice():
    prva = zaznajsnezinko(1)
    zadnja = zadnjazica(100)

    return zadnja - prva + 1 # če je snežina aktivirala samo 1 žico, je prva - zadnja = 0, zato dodamo 1


while True:
    x = zaznajsnezinko(1) # če je snežinka zaznana je x ena izmed aktiviranih žic
    if x:
        print(prestejzice())
        while Senzor(x): # dokler je ta žica aktivna, ne izpisujemo ničesar
            continue

