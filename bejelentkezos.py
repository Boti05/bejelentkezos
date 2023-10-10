profilok = {}
print("Üdvözöllek!\nEz egy bejelentkezős platform.")
mennyi = int(input("Hány profilt akarsz csinálni: "))
valid_felh_jelsz = False
#változókat hozok létre

while len(profilok.values()) < mennyi: 
    felh_nev = input("Írd be a felhasználónevet: ".strip())
    valid_felh_jelsz = False
    if felh_nev in profilok.keys():
        print("Ez a felhasználónév már foglalt.")
    elif "." in felh_nev or " " in felh_nev or felh_nev == "":
        print("A felhasználónév nem tartalmazhat se '.'-ot, se 'space'-t, de valamit tartalmaznia kell.")
    else:    
        while valid_felh_jelsz == False:
            jelszo = input("Írd be a jeszót: ".strip())
            if " " not in jelszo and len(jelszo) > 5:
                profilok.update({felh_nev : jelszo})
            else:
                print("Nem lehet a jelszóban szóköz és minimum 6 karakter legyen.")
            acces = input("Milyen típusú profilod lesz? Admin: 'a' vagy User: 'u': ")
            if acces == "a":
                admin = True
                valid_felh_jelsz = True
    print(profilok, len(profilok.values()))
    '''if acces == "a":
        del(profilok[felh_nev])
        profilok.update({felh_nev + "(admin)" : jelszo})
    if acces == "u":
        del(profilok[felh_nev])
        profilok.update({felh_nev + "(user)" : jelszo})'''
    

#annyiszor kérünk új felhasználónevet és jelszót, amennyit megadunk, ha foglalt a felhnév akkor kiírjuk és skipelünk


def belepes():
    global belepve 
    belepve = False
    belep_keres = True
    while belep_keres:
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
                    belepve = True
                if counter == 0 and siker == False:
                    print("Sajnálom többet nem próbálkozhatsz. :(")
        belep_keres = False
#ha van akkor bekérjük a jelszavát, ha nem jó a jelszó újrakérjük és egygyel kevesebb próbálkozása marad
belepes()
belepve = True
while belepve:
    if acces == "a":
        mi_kell = input(felh_nev + "(admin)> ")
        if mi_kell == "?" or mi_kell == "help":
            print("?                            -   kiírja a lehetőségeket")
            print("help                         -   kiírja a lehetőségeket")
            print("profilok mutatasa            -   kiírja az összes profil nevét")
            print("profilok mutatasa jelszoval  -   kiírja az összes profil nevét jelszóval")
            print("exit                         -   kilép a profilból (de nem törli azt)")
        if mi_kell == "profilok mutatasa":
            print(profilok.keys())
        if mi_kell == "profilok mutatasa jelszoval":
            print(f"{profilok.keys()} - {profilok.values()}")
        if mi_kell == "exit":
            belepve = False
            belepes()

#éasdklfj