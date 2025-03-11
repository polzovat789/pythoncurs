# Декоратор для проверки и конвертации типов параметров функции
def typed(type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Преобразуем все аргументы в указанный тип
            converted_args = [type(arg) for arg in args]
            converted_kwargs = {key: type(value) for key, value in kwargs.items()}

            # Вызываем исходную функцию с преобразованными аргументами
            return func(*converted_args, **converted_kwargs)

        return wrapper

    return decorator


# Пример использования декоратора для разных типов

@typed(type=str)
def add_str(a, b):
    return a + b


print(add_str("3", 5))  # Вывод: "35"
print(add_str(5, 5))  # Вывод: "55"
print(add_str('a', 'b'))  # Вывод: 'ab'


@typed(type=int)
def add_st(a, b, c):
    return a + b + c


print(add_st(5, 6, 7))  # Вывод: 18


@typed(type=float)
def add_strn(a, b, c):
    return a + b + c


print(add_strn(0.1, 0.2, 0.4))  # Вывод: 0.7000000000000001
