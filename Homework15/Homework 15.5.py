# Генератор чисел от 1 до N
def generate_numbers(N):
    for i in range(1, N + 1):
        yield i


# Генератор простых чисел
def generate_primes(start, end):
    for num in range(start, end + 1):
        if num < 2:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num


# Основная программа
if __name__ == "__main__":
    # Ввод числа N
    N = int(input("Введите целое число N: "))

    # Сумма чисел от 1 до N
    number_sum = sum(generate_numbers(N))
    print(f"Сумма чисел от 1 до {N}: {number_sum}")

    # Генерация и вывод первых 10 простых чисел от 1 до 100
    primes = generate_primes(1, 100)
    prime_count = 0
    for prime in primes:
        if prime_count < 10:
            print(prime, end=" ")
            prime_count += 1
        else:
            break
