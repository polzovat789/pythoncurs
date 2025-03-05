def cache(func):
    # Словарь для закэшированных результатов
    cached_results = {}

    def wrapper(*args):
        # Проверка, на результат в кэше
        if args in cached_results:
            return cached_results[args]

        # Если результата нет в кэше, вызвать функцию и сохранить результат
        result = func(*args)
        cached_results[args] = result
        return result

    return wrapper
