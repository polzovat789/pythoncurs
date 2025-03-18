def decorator(*args, **kwargs):
    def decorator_func(func):
        def wrapper(*f_args, **f_kwargs):
            # Формируем кортеж с позиционными аргументами и словарь с именованными
            result = (args, kwargs)
            # Выполняем исходную функцию
            func_result = func(*f_args, **f_kwargs)
            return result, func_result
        return wrapper
    return decorator_func

# Пример 1: использование декоратора с параметрами
@decorator(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', one=1, two=2, three=3)
def identity(x):
    return x

print(identity(42))
