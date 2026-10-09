"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""
from encodings import utf_8

# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))

with open("students.csv", encoding = "utf-8") as f:
    next(f)
    best_avg = 0
    students = 0
    best_name = ""
    sum_math = 0
    sum_english = 0
    sum_python = 0
    for line in f:
        line = line.strip()
        listt = line.split(",")
        list1 = listt[1::]
        list2 = [float(x) for x in list1]
        average = sum(list2)/len(list2)
        if average > best_avg:
            best_avg = average
            best_name = listt[0]
        students += 1
        sum_math += list2[0]
        sum_python += list2[1]
        sum_english += list2[2]
    avg_math = sum_math/students
    avg_english = sum_english/students
    avg_python = sum_python/students

with open("result.txt", "w", encoding = "utf-8") as f:
    f.write(f"Середній бал по класу:\n")
    f.write(f"math: {round(avg_math,1)} \n")
    f.write(f"python: {round(avg_python, 1)} \n")
    f.write(f"english: {round(avg_english, 1)} \n")
    f.write(f"\n")
    f.write(f"Найкращий студент: {best_name} ({round(best_avg,1)}) \n")
    print(f"Середній бал по класу:")
    print(f"math: {round(avg_math, 1)}")
    print(f"python: {round(avg_python, 1)}")
    print(f"english: {round(avg_english, 1)}")
    print(f"")
    print(f"Найкращий студент: {best_name}, ({round(best_avg, 1)})")
# TODO 2: пройдіться по рядках файлу (for line in f:), для кожного рядка:
#   - приберіть символ переносу рядка (line.strip())
#   - розбийте рядок по комі (line.split(","))
#   - перетворіть оцінки на числа (int або float)

# TODO 3: по ходу циклу накопичуйте:
#   - суми оцінок з кожного предмета та кількість студентів
#   - найкращого студента (ім'я та його середній бал) — порівнюйте
#     середній бал поточного студента з найкращим на цей момент

# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета
#   (сума / кількість студентів)


# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):
#
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.


# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
