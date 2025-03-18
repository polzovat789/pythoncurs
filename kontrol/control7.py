def build_symmetric_string(input_str, n):
    # Проверяем, что n не превышает длину строки input_str
    if n > len(input_str):
        raise ValueError("n не может быть больше длины строки input_str")

    # Берем первые n символов из строки input_str
    ascending = input_str[:n]

    # Создаем нисходящую часть (обратный порядок, исключая последний символ)
    descending = ascending[:-1][::-1]

    # Объединяем восходящую и нисходящую части
    symmetric_string = ascending + descending

    return symmetric_string


# Примеры использования
input_string = "abcdefghijklmnopqrstuvwxyz"
print(build_symmetric_string(input_string, 1))  # => "a"
print(build_symmetric_string(input_string, 2))  # => "aba"
print(build_symmetric_string(input_string, 3))  # => "abcba"
print(build_symmetric_string(input_string, 4))  # => "abcdcba"
print(build_symmetric_string(input_string, 5))  # => "abcdedcba"
