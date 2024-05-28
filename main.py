users: list[dict] = [
    {'name': 'Dominik', 'surname': 'Kuźnik', 'post': 1},
    {'name': 'Kacper', 'surname': 'Macioch', 'post': 2},
    {'name': 'Michał', 'surname': 'Krzywiński', 'post': 3},
    {'name': 'Tymon', 'surname': 'Leszczyc', 'post': 2},

]
def show_users(user_list: list[dict]) -> None:
    for user in user_list:
        print(f"Twój znajomy {user['name']} opublikował: {user['post']} postów")

if __name__ == '__main__':
    print:("Witaj użytkowniku")
    while True:

        print("Menu:")
        print("1. Wyświetl co u znajomych")
        menu_option:str=input("Dokonaj wyboru")
        if menu_option == "0":
            print("Program kończy pracę")
            break
        if menu_option == "1":
            show_users(users)

