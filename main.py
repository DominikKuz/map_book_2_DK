from models.data import users
from utils.crud import read, add_user


if __name__ == '__main__':
    print:('Witaj użytkowniku')
    while True:

        print('0. zakończ program')
        print('1. Wyświetl znajomych')
        print('2. dodaj znajomego')
        menu_option:str=input("Wybór")


        if menu_option == "0": break
        if menu_option == "1": read(users)
        if menu_option == "2": add_user(users)

