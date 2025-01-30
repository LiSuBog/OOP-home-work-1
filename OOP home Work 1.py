class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Student:

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_grade():.1f}'

    def get_average_grade(self):
        total = sum([sum(grades) for grades in self.grades.values()])
        count = sum([len(grades) for grades in self.grades.values()])
        return total / count if count > 0 else 0

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.get_average_grade():.1f}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def get_average_grade(self):
        total = sum([sum(grades) for grades in self.grades.values()])
        count = sum([len(grades) for grades in self.grades.values()])
        return total / count if count > 0 else 0

# Создание экземпляров
student_1 = Student('Ruoy', 'Eman', 'your_gender')
student_1.courses_in_progress.append('Python')
student_1.finished_courses.append('Введение в программирование')

student_2 = Student('John', 'Doe', 'your_gender')
student_2.courses_in_progress.append('Git')

lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached.append('Python')

reviewer_1 = Reviewer('Anna', 'Smith')
reviewer_1.courses_attached.append('Python')

# Использование методов
reviewer_1.rate_hw(student_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 9)

# Печать информации
print(reviewer_1)
print(lecturer_1)
print(student_1)

# Средняя оценка по всем студентам в рамках конкретного курса
def average_grade_students(students, course):
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return total / count if count > 0 else 0

# Средняя оценка по лекторам в рамках курса
def average_grade_lecturers(lecturers, course):
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total / count if count > 0 else 0

# Примеры вызова функций
print(f'Средняя оценка студентов по курсу Python: {average_grade_students([student_1, student_2], "Python"):.1f}')
print(f'Средняя оценка лекторов по курсу Python: {average_grade_lecturers([lecturer_1], "Python"):.1f}')