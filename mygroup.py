groupmates = [
    {
        "name": "Арсен",
        "surname": "Джабраилов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Владислав",
        "surname": "Авдеев",
        "exams": ["ОС", "ПИС", "МСиС"],
        "marks": [4, 4, 3]
    },
    {
        "name": "Анастасия",
        "surname": "Аксенова",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Филипп",
        "surname": "Бардин",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Михаил",
        "surname": "Виноградов",
        "exams": ["МиСПИСиТ", "АиГ", "АСиПРВ"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Алексей",
        "surname": "Гавриков",
        "exams": ["ОС", "Философия", "ПИС"],
        "marks": [3, 3, 5]
    }                
]

def print_students(students):
    print(u"Имя".ljust(15), 
        u"Фамилия".ljust(10), 
        u"Экзамены".ljust(30), 
        u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), 
        student["surname"].ljust(10), 
        str(student["exams"]).ljust(30), 
        str(student["marks"]).ljust(20))

def filter(students, avg_students):
    result = []
    for student in students:
        avg = sum(student["marks"]) / len(student["marks"])
        if avg > avg_students:
            result.append(student)
    return result

print("\nВведите минимальный средний балл:")
threshold = float(input())
filtered = filter(groupmates, threshold)
print("\nСтуденты со средним баллом выше", threshold, ":")
print_students(filtered)
