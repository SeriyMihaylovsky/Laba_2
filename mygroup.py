groupmates = [
    {
        "name": "Королева",
        "surname": "Виктория",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 5, 5]
    },
    {
        "name": "Михайловский",
        "surname": "Сергей",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [2, 2, 4]
    },
    {
        "name": "Бирюков",
        "surname": "Вячеслав",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 4, 3]
    },
    {
        "name": "Соколовский",
        "surname": "Михаил",
        "exams": ["Базы данных", "Web", "КТП"],
        "marks": [5, 5, 3]
    }
    {
        "name": "Уколов",
        "surname": "Кирилл",
        "exams": ["Физика", "Математика", "Информатика"],
        "marks": [2, 2, 5]
    },
]

def print_students(students):
    print(
        "Имя".ljust(15),
        "Фамилия".ljust(15),
        "Экзамены".ljust(30),
        "Оценки".ljust(20),
        "Ср. балл".ljust(10),
    )
    for student in students:
        avg_mark = sum(student["marks"]) / len(student["marks"])
        print(
            student["name"].ljust(15),
            student["surname"].ljust(15),
            str(student["exams"]).ljust(30),
            str(student["marks"]).ljust(20),
            f"{avg_mark:.2f}".ljust(10)
        )


def filter_by_average(students, min_avg):
    result = []
    for student in students:
        avg_mark = sum(student["marks"]) / len(student["marks"])
        if avg_mark > min_avg:
            result.append(student)
    return result

try:
    threshold = float(input("Введите минимальный средний балл: "))
except ValueError:
    print("Ошибка: нужно ввести число!")
else:
    filtered = filter_by_average(groupmates, threshold)

    if filtered:
        print("\nСтуденты с средним баллом выше", threshold, ":\n")
        print_students(filtered)
    else:
        print("Нет таких студентов.")
