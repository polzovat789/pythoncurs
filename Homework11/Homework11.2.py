# Декоратор для проверки, что результат функции является числом
def validate_result(func):
    def wrapper(*args, **kwargs):
        # Выполнение функции и получение результата
        result = func(*args, **kwargs)

        # Проверка, что результат является числом (int или float)
        if not isinstance(result, (int, float)):
            print("Ошибка: Результат функции не является числом!")
        else:
            return result

    return wrapper


# Пример функции с декоратором validate_result
@validate_result
def multiply(a, b):
    return a * b  # Эта функция возвращает число


@validate_result
def greet(name):
    return f"Hello, {name}!"  # Эта функция возвращает строку, не число


# Вызов функции, результат которой является числом
print(multiply(2, 3))  # Вывод: 6

# Вызов функции, результат которой не является числом
print(greet("Alice"))  # Вывод: Ошибка: Результат функции не является числом!
