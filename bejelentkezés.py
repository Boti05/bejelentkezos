profilok = {}
print("Üdvözöllek!\nEz egy bejelentkezős platform.")
mennyi = int(input("Hány profilt akarsz csinálni: "))
valid_felh_jelsz = False
#változókat hozok létre

while len(profilok.values()) < mennyi: 
    felh_nev = input("Írd be a felhasználónevet: ".strip())
    if felh_nev in profilok.keys():
        print("Ez a felhasználónév már foglalt.")
    if "." in felh_nev or " " in felh_nev or felh_nev == "":
        print("A felhasználónév nem tartalmazhat se '.'-ot, se 'space'-t, de valamit tartalmaznia kell.")
    else:    
        while valid_felh_jelsz == False:
            jelszo = input("Írd be a jeszót: ".strip())
            if " " not in jelszo and len(jelszo) > 5:
                profilok.update({felh_nev : jelszo})
                valid_felh_jelsz = True
            else:
                print("Nem lehet a jelszóban szóköz és minimum 6 karakter legyen.")
#annyiszor kérünk új felhasználónevet és jelszót, amennyit megadunk, ha foglalt a felhnév akkor kiírjuk és skipelünk

print(profilok)

print("Most jelentkezzünk be valamelikbe.")
siker = False
melyik = input("Melyik felhasználó profiljába jelentkezzünk be (írd be a felhasználónevet): ")
while melyik not in profilok.keys():
    print("Ilyen felhasználónevű profil nincs. Próbálkozz másikkal.")
    melyik = input("Melyik felhasználó profiljába jelentkezzünk be (írd be a felhasználónevet): ")
#megnézzük, hogy melyik profilba akarunk bejelentkezni, ha nincs ilyen profil akkor újra kérjük

else: 
    counter = 3
    melyik_jelszo = input("Most írd be a jelszót: ")
    if profilok[melyik] != melyik_jelszo and counter > 0:
        counter -= 1
        print(f"Nem jó a jelszó!\nMár csak {counter} alkalommal próbálkozhatsz!")
    while profilok[melyik] != melyik_jelszo and counter > 0:
        melyik_jelszo = input("Most írd be a jó jelszót: ")
        counter -= 1
        if counter >= 0 and profilok[melyik] != melyik_jelszo:
            print(f"Nem jó a jelszó!\nMár csak {counter} alkalommal próbálkozhatsz!")
    else: 
        if counter >= 0 and profilok[melyik] == melyik_jelszo:
            print("Gratulálok, beléptél!")
            siker = True
        if counter == 0 and siker == False:
            print("Sajnálom többet nem próbálkozhatsz. :(")
#ha van akkor bekérjük a jelszavát, ha nem jó a jelszó újrakérjük és egygyel kevesebb próbálkozása marad
