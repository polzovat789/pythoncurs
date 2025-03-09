# Декоратор для кэширования результатов вызова функции
def cache(func):
    cached_results = {}  # Словарь для хранения закэшированных значений

    def wrapper(*args):
        # Проверка, есть ли уже результат для таких аргументов в кэше
        if args in cached_results:
            return cached_results[args]  # Возвращаем закэшированный результат
        else:
            result = func(*args)  # Если нет, вызываем функцию
            cached_results[args] = result  # Сохраняем результат в кэше
            return result

    return wrapper

# Пример использования декоратора @cache
@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Вызов функции и использование кэширования
print(fibonacci(5))  # Вывод: 5 (рассчитывается, результат сохраняется)
print(fibonacci(10))  # Вывод: 55 (рассчитывается, результат сохраняется)
print(fibonacci(5))  # Вывод: 5 (значение взято из кэша)
