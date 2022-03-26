# naredimo seznam vseh možnih kombinacij stranic
# iz tega seznama najprej poiščemo, katera kombinacija stranic nam da razmerje med njima čim bližje 1, to je velikost pravokotnika, ki ga moramo izpisati

# ker se vsi pravokotniki začnejo pri (0, 0) lahko najdemo vse možne kombinacije:
a = 0
visine, sirine = [], []
razmerja = {}

for i in sirine:
    a += i
    b = 0
    for j in visine:
        b += j
        razmerja.update({int(a/b): (a, b)})
    
raz = list(razmerja.keys())
raz.sort()


# v spremenljivki najblizji je mesto kombinacije stranic v razmerja ki je najbližje 1 -> kvadratu
# ker morda obstaja razmerje, ki je 1 še bližje, nadaljujemo s preverjanjem
# najbližji posodobimo, če najdemo število, ki je bližje 1
# razliko s številom 1 izračunamo kot absolutno vrednost razlike med 1 in številom
najblizji = 0
for i in raz:
    if abs(1-i) < abs(1-najblizji):
        najblizji = i


print(razmerja[najblizji])