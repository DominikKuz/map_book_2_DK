class User:
    def __init__(self, imie, nazwisko, posty, miejscowosc):
        self.imie = imie
        self.nazwisko = nazwisko
        self.posty = posty
        self.miejscowosc = miejscowosc



zmienna_w_pamieci_na_uzytkownika_1=User(imie='Kacper',nazwisko='Macioch',posty='4',miejscowosc='Ząbki')
zmienna_w_pamieci_na_uzytkownika_2=User(imie='Dominik',nazwisko='Kuźnik',posty='4',miejscowosc='Ząbki')
print(zmienna_w_pamieci_na_uzytkownika_1)
print(zmienna_w_pamieci_na_uzytkownika_2)
