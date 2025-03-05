def typed(type_):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Конвертируем аргументы
            converted_args = [type_(arg) for arg in args]
            converted_kwargs = {
                key: type_(value) for key, value in kwargs.items()}

            # Вызываем функцию с аргументами
            result = func(*converted_args, **converted_kwargs)

            # Возвращение результата в нужный тип
            return type_(result)

        return wrapper

    return decorator
