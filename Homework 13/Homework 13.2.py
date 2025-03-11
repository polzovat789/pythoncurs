class CurrencyConverter:
    # Курсы валют относительно BYN (можно расширить другими валютами)
    exchange_rates = {
        'USD': 3.269,  # 1 USD = 3.269 BYN
        'EUR': 3.2,  # 1 EUR = 3.2 BYN
        'BYN': 1,  # 1 BYN = 1 BYN
    }

    @staticmethod
    def exchange_currency(currency, amount, target_currency='BYN'):
        # Проверяем, если целевая валюта и исходная валюта одинаковы
        if currency == target_currency:
            return amount, target_currency

        # Получаем курс валют относительно BYN
        if currency not in CurrencyConverter.exchange_rates:
            raise ValueError(f"Неизвестная валюта: {currency}")
        if target_currency not in CurrencyConverter.exchange_rates:
            raise ValueError(f"Неизвестная валюта: {target_currency}")

        # Конвертируем в BYN
        amount_in_byn = amount * CurrencyConverter.exchange_rates[currency]

        # Конвертируем в целевую валюту
        amount_in_target = amount_in_byn / CurrencyConverter.exchange_rates[target_currency]

        return round(amount_in_target, 2), target_currency


class Person:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount


# Тестирование
converter = CurrencyConverter()

# Создаем два объекта Person с разными валютами
vasya = Person('USD', 10)
petya = Person('EUR', 5)

# Конвертация в BYN
assert (converter.exchange_currency(vasya.currency, vasya.amount)
        == (32.69, "BYN")), "Ошибка конвертации для Васи"
assert (converter.exchange_currency(petya.currency, petya.amount)
        == (35.2, "BYN")), "Ошибка конвертации для Пети"

# Конвертация в заданную валюту
assert (converter.exchange_currency(vasya.currency, vasya.amount, 'EUR')
        == (9.29, "EUR")), "Ошибка конвертации для Васи в EUR"
assert (converter.exchange_currency(petya.currency, petya.amount, 'USD')
        == (10.76, "USD")), "Ошибка конвертации для Пети в USD"

print("Все тесты пройдены успешно!")
