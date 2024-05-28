from tkinter import *

def prosta_funkcja():
    print("Prosta funkcja.")

root = Tk()
root.geometry("800x700")
root.title("Map Book DK")


# ramki do porządkowania struktury
ramka_lista_uzytkownikow=Frame(root)
ramka_formularz=Frame(root)
ramka_pokaz_szczegoly=Frame(root)
ramka_mapa=Frame(root)


ramka_lista_uzytkownikow.grid(column=0, row=0,padx=50)
ramka_formularz.grid(column=1, row=0)
ramka_pokaz_szczegoly.grid(column=0, row=1,columnspan=2,padx=50,pady=20)
ramka_mapa.grid(column=0, row=2)


# ramka lista uzytkownikow
Label_lista_uzytkownikow=Label(ramka_lista_uzytkownikow, text="lista użytkowników")
Listbox_lista_uzytkownikow=Listbox(ramka_lista_uzytkownikow,width=30)
button_pokaz_szczegoly=Button(ramka_lista_uzytkownikow,text="pokaż szczegóły")
button_edytuj_uzytkownika=Button(ramka_lista_uzytkownikow,text="edytuj")
button_usun_uzytkownika=Button(ramka_lista_uzytkownikow,text="usuń")

Label_lista_uzytkownikow.grid(column=0, row=0)
Listbox_lista_uzytkownikow.grid(column=0, row=1,columnspan=3)
button_pokaz_szczegoly.grid(column=0, row=2)
button_edytuj_uzytkownika.grid(column=1, row=2)
button_usun_uzytkownika.grid(column=2, row=2)

# ramka formularz

Label_formularz=Label(ramka_formularz, text="Formularz edycjii i dodawania")
Label_imie=Label(ramka_formularz, text="Imię")
Label_nazwisko=Label(ramka_formularz, text="Nazwisko")
Label_posty=Label(ramka_formularz, text="Posty")
Label_miejscowosc=Label(ramka_formularz, text="Miejscowość")
entry_imie=Entry(ramka_formularz)
entry_nazwisko=Entry(ramka_formularz)
entry_posty=Entry(ramka_formularz)
entry_miejscowosc=Entry(ramka_formularz)
button_dodaj_uzytkownika=Button(ramka_formularz,text="Dodaj")




Label_formularz.grid(column=0, row=0, columnspan=2)
Label_imie.grid(column=0, row=1,sticky=W)
Label_nazwisko.grid(column=0, row=2,sticky=W)
Label_posty.grid(column=0, row=3,sticky=W)
Label_miejscowosc.grid(column=0, row=4,sticky=W)

entry_imie.grid(column=1, row=1)
entry_nazwisko.grid(column=1, row=1)
entry_posty.grid(column=1, row=2)
entry_miejscowosc.grid(column=1, row=3)
button_dodaj_uzytkownika.grid(column=0, row=5,columnspan=2)

#ramka_pokaz_szczegoly
Label_opis_uzytkownika=Label(ramka_pokaz_szczegoly, text="Szczegóły użytkownika")
Label_imie_szczegoly=Label(ramka_pokaz_szczegoly,text="Imię")
Label_imie_szczegoly_wartosc=Label(ramka_pokaz_szczegoly,text="...",width=10)
Label_nazwisko=Label(ramka_pokaz_szczegoly, text="Nazwisko")
Label_nazwisko_wartosc=Label(ramka_pokaz_szczegoly, text="...",width=10)
Label_posty_szczegoly=Label(ramka_pokaz_szczegoly,text="...")
Label_posty_szczegoly_wartosc=Label(ramka_pokaz_szczegoly,text="...",width=10)
Label_miejscowosc=Label(ramka_pokaz_szczegoly,text="Miejscowość")
Label_miejscowosc_wartosc=Label(ramka_pokaz_szczegoly,text="...",width=10)

Label_opis_uzytkownika.grid(column=0, row=0)
Label_imie_szczegoly.grid(column=0, row=1)
Label_imie_szczegoly_wartosc.grid(column=1, row=1)
Label_nazwisko.grid(column=2, row=1)
Label_nazwisko_wartosc.grid(column=3, row=1)
Label_posty_szczegoly.grid(column=4, row=1)
Label_posty_szczegoly_wartosc.grid(column=5,row=1)
Label_miejscowosc.grid(column=6, row=1)
Label_miejscowosc_wartosc.grid(column=7, row=1)








root.mainloop()