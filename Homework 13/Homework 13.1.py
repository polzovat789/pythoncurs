import random


class Card:
    # Списки номеров карт и мастей
    number_list = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
    mast_list = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    def __init__(self, mast, number):
        self.mast = mast
        self.number = number

    def __str__(self):
        return f'{self.mast} {self.number}'


class CardsDeck:
    def __init__(self):
        # Создаем колоду из 52 карт + 2 джокера
        self.cards = [Card(mast, number) for mast in Card.mast_list
                      for number in Card.number_list] + ['Joker', 'Joker']

    def shuffle(self):
        # Перемешиваем колоду
        random.shuffle(self.cards)

    def get(self, card_number):
        # Получаем карту по ее номеру (индекс в списке)
        if 1 <= card_number <= 54:
            return self.cards[card_number - 1]
        else:
            return 'Неверный номер карты'


# Пример использования
deck = CardsDeck()
deck.shuffle()

# Запрос у пользователя карты
card_number = int(input('Выберите карту из колоды в 54 карты: '))
card = deck.get(card_number)
print(f'Ваша карта: {card}')

card_number = int(input('Выберите карту из колоды в 54 карты: '))
card = deck.get(card_number)
print(f'Ваша карта: {card}')
