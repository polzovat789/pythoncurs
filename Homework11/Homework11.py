def validate_arguments(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(
                    f"Аргумент {arg} не является положительным числом")

        for key, value in kwargs.items():
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError(
                    f"Аргумент {key}={value} не является положительным числом")

        return func(*args, **kwargs)

    return wrapper
