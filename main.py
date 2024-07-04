from models.data import radios, transmitters, employees, clients
from utils.crud import show_radio, add_new_radio, delete_radio, edit_radio, show_transmitters, add_transmitters, delete_transmitter, update_transmitter, show_employees, add_employee, delete_employee, update_employee, show_clients, radio_employees, radio_clients, map_radios, map_transmitters, map_employees

def login():
    print("logowanie")
    username = input("Nazwa użytkownika: ")
    password = input("Hasło: ")
    if username == "Dominik" and password == "Dominik":
        print("zalogowano")
        return True
    else:
        print("nie zalogowano")
        return False
if __name__ == "__main__":
        if login():
            while True:
                print('0. zakończ program ')
                print('1. wyświetl stacje radiowe ')
                print('2. dodaj stację ')
                print('3. usuń stację')
                print('4. edytuj stację ')
                print('5. wyświetl nadajniki')
                print('6. dodaj nadajnik')
                print('7. usuń nadajnik')
                print('8. edytuj nadajnik')
                print('9. wyświetl pracowników')
                print('10. dodaj pracownika')
                print('11. usuń pracownika')
                print('12. edytuj pracownika')
                print('13. wyświetl wszystkich klientów')
                print('14. wyświetl klientów wybranej stacji radiowej')
                print('15. wyświetl pracowników wybranej stacji radiowej')
                print('16. pokaż mapę stacji radiowych')
                print('17. pokaż mapę nadajników')
                print('18. pokaż mapę pracowników')
                menu_option = input('wybierz opcje menu: ')
                if menu_option == '0': break
                if menu_option == '1': show_radio(radios)
                if menu_option == '2': add_new_radio(radios)
                if menu_option == '3': delete_radio(radios)
                if menu_option == '4': edit_radio(radios)
                if menu_option == '5': show_transmitters(transmitters)
                if menu_option == '6': add_transmitters(transmitters)
                if menu_option == '7': delete_transmitter(transmitters)
                if menu_option == '8': update_transmitter(transmitters)
                if menu_option == '9': show_employees(employees)
                if menu_option == '10': add_employee(employees)
                if menu_option == '11': delete_employee(employees)
                if menu_option == '12': update_employee(employees)
                if menu_option == '13': show_clients(clients)
                if menu_option == '14': radio_clients(radios, clients)
                if menu_option == '15': radio_employees(radios, employees)
                if menu_option == '16': map_radios(radios)
                if menu_option == '17': map_transmitters(transmitters)
                if menu_option == '18': map_employees(employees)



