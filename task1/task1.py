"""
У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. 
Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.

Наприклад:

Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000

Ваше завдання - розробити функцію total_salary(path), яка аналізує цей файл і повертає загальну та середню суму заробітної плати всіх розробників.

Вимоги до завдання:

Функція total_salary(path) має приймати один аргумент - шлях до текстового файлу (path).
Файл містить дані про заробітні плати розробників, розділені комами. Кожен рядок вказує на одного розробника.
Функція повинна аналізувати файл, обчислювати загальну та середню суму заробітної плати.
Результатом роботи функції є кортеж із двох чисел: загальної суми зарплат і середньої заробітної плати.

Рекомендації для виконання:

Використовуйте менеджер контексту with для читання файлів.
Пам'ятайте про встановлення кодування при відкриті файлів
Для розділення даних у кожному рядку можна застосувати метод split(',').
Обрахуйте загальну суму заробітної плати, а потім розділіть її на кількість розробників, щоб отримати середню зарплату.
Опрацьовуйте можливі винятки при роботі з файлами, такі як відсутність файлу.

Критерії оцінювання:

Функція повинна точно обчислювати загальну та середню суми.
Повинна бути обробка випадків, коли файл відсутній або пошкоджений.
Код має бути чистим, добре структурованим і зрозумілим.

Приклад використання функції:

total, average = total_salary("path/to/salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

Очікуваний результат:

Загальна сума заробітної плати: 6000, Середня заробітна плата: 2000

"""


def total_salary(path: str) -> str:
    """
    Return string with sum of salaries and average salary from inpur file in format Name, Salary.

    Args:
        path - path to the file.

    Returns:
        string with salary data.

    Raises:
        if path/data wrong returns an empty string.
    """
    if not path:
        return ""

    try:
        # Open file and read data from it
        with open(path, mode="r", encoding="utf-8") as data:
            # Read all lines from file
            lines = data.readlines()
            # Create array of salaries from data
            try:
                salaries = [float(line.split(",")[-1]) for line in lines]
            except:
                print("Wrong data in the file.")
                return ""
            # Return string
            return f"Загальна сума заробітної плати: {sum(salaries):.0f}, Середня заробітна плата: {sum(salaries) / len(salaries):.0f}"
    except FileNotFoundError:
        print("File does not exist in the script directory")
        return ""
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return ""


# Tests
test1 = total_salary("task_1_1.txt")
print(test1)
test2 = total_salary("task_1_2.txt")
print(test2)