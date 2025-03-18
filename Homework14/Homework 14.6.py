import json


# Чтение JSON и нахождение клуба с наибольшими победами
def club_with_most_wins(json_file):
    with open(json_file, 'r') as f:
        clubs = json.load(f)
    max_wins_club = max(clubs, key=lambda x: x['wins'])
    return max_wins_club


try:
    club = club_with_most_wins('clubs.json')
    print(f"Клуб с наибольшими победами: {club['name']} ({club['wins']} побед)")
except FileNotFoundError:
    print("Файл не найден!")
