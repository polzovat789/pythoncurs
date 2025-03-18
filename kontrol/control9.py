import random

# Класс солдата
class Soldier:
    def __init__(self, soldier_id, team):
        self.soldier_id = soldier_id
        self.team = team

    def move_to_hero(self, hero):
        print(f"Солдат {self.soldier_id} теперь следует за героем {hero.hero_id} команды {hero.team}")

# Класс героя
class Hero:
    def __init__(self, hero_id, team):
        self.hero_id = hero_id
        self.team = team
        self.level = 1

    def level_up(self):
        self.level += 1
        print(f"Герой {self.hero_id} из команды {self.team} поднимет уровень: {self.level}")

# Основная программа
def game():
    # Создаем героев
    hero_1 = Hero(hero_id=1, team="Team A")
    hero_2 = Hero(hero_id=2, team="Team B")

    # Генерация солдат для двух команд
    team_a_soldiers = [Soldier(i, "Team A") for i in range(1, 11)]
    team_b_soldiers = [Soldier(i, "Team B") for i in range(1, 11)]

    # Измеряем длину команд
    print(f"Команда {hero_1.team} имеет {len(team_a_soldiers)} солдат.")
    print(f"Команда {hero_2.team} имеет {len(team_b_soldiers)} солдат.")

    # Увеличиваем уровень герою, у которого больше солдат
    if len(team_a_soldiers) > len(team_b_soldiers):
        hero_1.level_up()
    else:
        hero_2.level_up()

    # Солдат первого героя следует за ним
    soldier_to_follow = team_a_soldiers[0]
    soldier_to_follow.move_to_hero(hero_1)

    # Выводим информацию о герое и солдате
    print(f"Герой {hero_1.hero_id} из команды {hero_1.team}")
    print(f"Солдат {soldier_to_follow.soldier_id} следит за героем {hero_1.hero_id}")

# Запуск игры
game()
