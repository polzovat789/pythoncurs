# Функция для подсчета суммы всех чисел до заданного числа
def sum_of_numbers(n):
    # Сумма всех чисел от 1 до n
    return n * (n + 1) // 2  # Используем целочисленное деление для получения целого результата

# Примеры использования функции
print(sum_of_numbers(1))   # 1
print(sum_of_numbers(8))   # 36
print(sum_of_numbers(22))  # 253
print(sum_of_numbers(100)) # 5050
