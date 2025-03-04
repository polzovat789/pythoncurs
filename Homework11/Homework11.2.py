def validate_return_type(func):
    def wrapper(*args, **kwargs):
        # Вызов
        result = func(*args, **kwargs)

        # Проверка
        if not isinstance(result, (int, float)):
            print(f"Ошибка: результат {result} не является числом")
        else:
            # Если результат корректен, возвращаем его
            return result

    return wrapper
