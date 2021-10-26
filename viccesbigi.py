from collections import Counter
#  [0]     [1]  [2]    [3]
#Helyezes;Nev;Orszag;Nyeremeny

with open("snooker.txt") as f:
    lista = []
    elso_sor = f.readline()
    for sor in f:        sor = sor.strip().split(";");        lista.append(sor)

#3.feladat        
versenyzok_szama = len(lista);print(f"3.feladat: A világranglistán {versenyzok_szama} versenyző szerepel")

#4.feladat
szamok = [];
for sor in lista:    szamok.append(int(sor[3]))
    
ossz = sum(szamok)
atlag = ossz / versenyzok_szama;print(f"4.feladat: A versenyzők {atlag:.2f} fontot kerestek")

#5.feladat
kinaiak = []
for sor in lista:
    if sor[2] == "Kína":        kinaiak.append(sor)
        
a_kinai = []        
szam  = 0        
for sor in kinaiak:
    if int(sor[3]) > szam:        szam = int(sor[3]);        a_kinai = sor;print(f"5.feladat: A legjobban kereső kínai versenyző: \nHelyezés {a_kinai[0]} \nNév: {a_kinai[1]} \nország:: {a_kinai[2]} \nNyeremény összege: {int(a_kinai[3])*380}")

#6.feladat
nv_kerdes = "nincs"
for sor in lista:
    if sor[2] == "Norvégia":        nv_kerdes = "Van";print(f"6.feladat: A versenyzők között {nv_kerdes} norvég versenyző")

#7.feladat

osz = Counter(sor[2] for sor in lista);print("7.feladat: Statisztika")
for orszag, db in osz.items():
    if db > 4:        print(f"{orszag} - {db} fő")

    
    
        

    
 


