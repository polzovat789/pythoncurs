def validate_arguments(func):
    def wrapper(*args, **kwargs):
        # Проверяем позиц-ные аргументы
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"Аргумент {arg} не является положительным числом")

        # Проверяем именованные аргументы
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError(f"Аргумент {key}={value} не является положительным числом")

        # Если все аргументы корректны, вызываем исходную функцию
        return func(*args, **kwargs)

    return wrapper
