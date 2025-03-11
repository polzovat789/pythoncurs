# Декоратор для проверки, что все аргументы функции являются положительными числами
def validate_arguments(func):
    def wrapper(*args, **kwargs):
        # Перебираем все аргументы функции
        for arg in args:
            # Проверка, что аргумент является положительным числом
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"Аргумент {arg} должен быть положительным числом")
        # Выполняем исходную функцию, если все аргументы валидны
        return func(*args, **kwargs)
    return wrapper


# Пример функции с декоратором validate_arguments
@validate_arguments
def add_numbers(a, b):
    return a + b


# Вызовы функции с положительными аргументами
print(add_numbers(5, 10))  # Вывод: 15

# Вызов с отрицательным аргументом, который вызовет исключение
try:
    print(add_numbers(-5, 10))
except ValueError as e:
    print(e)  # Вывод: Аргумент -5 должен быть положительным числом

# Вызов с аргументом, не являющимся числом, который также вызовет исключение
try:
    print(add_numbers(5, "10"))
except ValueError as e:
    print(e)  # Вывод: Аргумент 10 должен быть положительным числом
