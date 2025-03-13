# Создаем файл students.txt, если его нет
try:
    with open('students.txt', 'x') as f:
        students = [
            ("Иванов", "A1", 5),
            ("Петров", "A2", 4),
            ("Сидоров", "A1", 3),
            ("Кузнецов", "A3", 5)
        ]
        for student in students:
            f.write(f'{student[0]} {student[1]} {student[2]}\n')
except FileExistsError:
    pass  # Файл уже существует, не делаем ничего

# Открываем файл для чтения и анализа
try:
    with open('students.txt', 'r') as f:
        students_data = f.readlines()
        total_students = len(students_data)
        groups = {}

        # Подсчитываем количество студентов и среднюю оценку по группам
        for line in students_data:
            # Разделяем строку на фамилию, группу и оценку
            name, group, grade = line.strip().split()
            # Преобразуем оценку в целое число
            grade = int(grade)

            if group not in groups:
                groups[group] = {"count": 0, "sum": 0}

            # Обновляем количество студентов и сумму оценок для группы
            groups[group]["count"] += 1
            groups[group]["sum"] += grade

        # Выводим результаты
        print(f"Общее количество студентов: {total_students}")
        for group, data in groups.items():
            avg_grade = data["sum"] / data["count"]
            print(f"Группа {group}: {data['count']} студентов, "
                  f"средняя оценка {avg_grade:.2f}")

        # Записываем статистику в файл
        with open('students.txt', 'a') as f_append:
            f_append.write(f"\nОбщее количество студентов: {total_students}\n")
            for group, data in groups.items():
                avg_grade = data["sum"] / data["count"]
                f_append.write(f"Группа {group}: {data['count']} студентов, "
                               f"средняя оценка {avg_grade:.2f}\n")

except FileNotFoundError:
    print("Файл не найден!")
