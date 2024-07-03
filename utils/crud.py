import folium
import requests
from bs4 import BeautifulSoup
from models.data import radios, clients


def show_radio(radio: list[dict[str, str]]) -> None:
    for radio in radios:
        print(f"Nazwa: {radio['name']} , Czestotliwosc: {radio['frequency band']} , Lokalizacja: {radio['location']}")


def add_new_radio(radio: list[dict[str, str]]) -> None:
    name = input("Nazwa: ")
    frequency = input("czestotliwosc: ")
    location = input("lokalizacja: ")
    new_radio = {"name": name, "frequency band": frequency, "location": location}
    print(new_radio)
    radio.append(new_radio)


def delete_radio(radio: list[dict[str, str]]) -> None:
    radio_name = input("jaką stację usunąć?: ")
    for radio in radios:
        if f"{radio['name']}" == radio_name:
            radios.remove(radio)


def edit_radio(radio: list[dict[str, str]]) -> None:
    radio_name = input("jaką stację uaktualnić?: ")
    for radio in radios:
        if f"{radio['name']}" == radio_name:
            radio["name"] = input("Nazwa stacji: ")
            radio["frequency band"] = input("częstotliwość: ")
            radio["location"] = input("lokalizacja: ")
            print(radios)
            radios.append(radio)


def show_transmitters(transmitters: list[dict]) -> None:
    for transmitter in transmitters:
        print(f" nadajnik: {transmitter['name']}, location: {transmitter['location']}")


def add_transmitters(transmitters: list[dict]) -> None:
    transmitter_name = input("Nazwa nadajnika: ")
    transmitter_location = input("lokalizacja: ")
    new_transmitter = {"Nazwa nadajnika": transmitter_name, "lokalizacja": transmitter_location}
    print(new_transmitter)
    transmitters.append(new_transmitter)


def delete_transmitter(transmitters: list[dict]) -> None:
    transmitter_name = input("Który nadajnik usunąć?: ")
    for transmitter in transmitters:
        if transmitter['name'] == transmitter_name:
            transmitters.remove(transmitter)


def update_transmitter(transmitters: list[dict])-> None:
    transmitter_name = input("Który nadajnik edytować: ")
    for transmitter in transmitters:
        if transmitter['name'] == transmitter_name:
            transmitter['name'] = input("Nadajnik: ")
            transmitter['location'] = input("Lokalizacja: ")
            transmitters.append(transmitter)


def show_employees(employees_list: list[dict]) -> None:
    for employee in employees_list:
        print(
            f"{employee['name']} {employee['surname']}, radio: {employee['radio']}, mieszka w: {employee['location']}")


def add_employee(employees: list) -> None:
    employee_name = input("Imie: ")
    employee_surname = input("Nazwisko: ")
    employee_radio = input("Radio: ")
    employee_location = input("Mieszka w: ")
    new_employees = {'name': employee_name, 'surname': employee_surname, 'restaurant': employee_radio,
                     'location': employee_location}
    employees.append(new_employees)


def delete_employee(employees: list) -> None:
    employee_name = input("Kogo usunąć?: ")
    for employee in employees:
        if f"{employee['name']}" == employee_name:
            employees.remove(employee)


def update_employee(employees: list) -> None:
    employee_name = input("Kogo edytować?: ")
    for employee in employees:
        if f"{employee['name']}" == employee_name:
            employee['name'] = input("Imie: ")
            employee['surname'] = input("Nazwisko: ")
            employee['radio'] = input("Radio: ")
            employee['location'] = input("mieszka w: ")
            employees.append(employee)


def show_clients(clients_list: list[dict]) -> None:
    for clients in clients_list:
        print(
            f"{clients['name']} {clients['surname']}, radio: {clients['radio']}")

def radio_employees(radios: list[dict[str, str]], employees: list[dict]) -> None:
    radio_name = input("Podaj nazwę stacji: ")
    for radio in radios:
        if radio_name == radio['name']:
            for employer in employees:
                if employer['radio'] == radio_name:
                    print(f" pracownik  : {employer['name']}")


def radio_clients(radios: list[dict[str, str]], clients: list[dict]) -> None:
    radio_name = input("Podaj nazwę stacji: ")
    for radio in radios:
        if radio_name == radio['name']:
            for client in clients:
                if client['radio'] == radio_name:
                    print(f" klient  : {client['name']}")


def map_radios(radios):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for radio in radios:
        url = (f"https://pl.wikipedia.org/wiki/{radio['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{radio['name']},\n{radio['location']}",
                      icon=folium.Icon(color='red')).add_to(map)

    map.save('utils/map_radio.html')


def map_employees(employees):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for employee in employees:
        url = (f"https://pl.wikipedia.org/wiki/{employee['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{employee['name']},\n{employee['location']}",
                      icon=folium.Icon(color='blue')).add_to(map)

    map.save('utils/map_employees.html')


def map_transmitters(transmitters):
    map = folium.Map(location=[52, 20], zoom_start=6)
    for transmitter in transmitters:
        url = (f"https://pl.wikipedia.org/wiki/{transmitter['location']}")
        response = requests.get(url)
        response_html = BeautifulSoup(response.text, 'html.parser')
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        print(longitude, latitude)
        folium.Marker(location=[latitude, longitude],
                      popup=f"{transmitter['name']},\n{transmitter['location']}",
                      icon=folium.Icon(color='purple')).add_to(map)

    map.save('utils/map_transmitters.html')