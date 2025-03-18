def count_and_update_file(path_to_file):
    try:
        # Чтение файла
        with open(path_to_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # Подсчет количества строк, слов и букв
        lines = content.splitlines()
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        num_letters = sum(len(line) for line in lines)

        # Формирование строки с информацией
        info = f"\n\nКоличество строк: {num_lines}\n"
        info += f"Количество слов: {num_words}\n"
        info += f"Количество букв: {num_letters}"

        # Вывод информации на экран
        print(info)

        # Дописывание информации в файл
        with open(path_to_file, 'a', encoding='utf-8') as file:
            file.write(info)

        print(f"Информация успешно дописана в файл: {path_to_file}")

    except FileNotFoundError:
        print(f"Файл {path_to_file} не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Пример использования
file_path = 'example.txt'  # Укажите путь к вашему файлу
count_and_update_file(file_path)
