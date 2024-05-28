users: list[dict] = [
    {'name': 'Dominik', 'surname': 'Kuźnik', 'post': 1},
    {'name': 'Kacper', 'surname': 'Macioch', 'post': 2},
    {'name': 'Michał', 'surname': 'Krzywiński', 'post': 3},
    {'name': 'Tymon', 'surname': 'Leszczyc', 'post': 2},
]

for user in users:
    print(f"Twój znajomy {user['name']} opublikował: {user['post']} postów")