class Student:
    instance_list_s = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grades = 0
        Student.instance_list_s.append(self)

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 0 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(self):
        if sum([len(i) for i in self.grades.values()]) > 0:
            result = round(sum([sum(i) for i in self.grades.values()]) / sum([len(i) for i in self.grades.values()]), 2)
            self.average_grades = result
            return result

    def completion_course(self, course):
        self.finished_courses.append(course)
        self.courses_in_progress.remove(course)

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                 f'Средняя оценка за домашние задания: {self.average_grades}\n' \
                 f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
                 f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return result

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.average_rating() > other.average_rating()
        print('Ошибка')
        return

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.average_rating() == other.average_rating()
        print('Ошибка')
        return


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    instance_list_l = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grades_l = 0
        Lecturer.instance_list_l.append(self)

    def average_rating(self):
        if sum([len(i) for i in self.grades.values()]) > 0:
            result = round(sum([sum(i) for i in self.grades.values()]) /
                           sum([len(i) for i in self.grades.values()]), 2)
            self.average_grades_l = result
            return result

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                 f'Средняя оценка за лекции: {self.average_grades_l}'
        return result

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.average_rating() > other.average_rating()
        print('Ошибка')
        return

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.average_rating() == other.average_rating()
        print('Ошибка')
        return


class Reviever(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_rev(self, student, course, grade):
        if isinstance(student,
                      Student) and course in self.courses_attached and course in student.courses_in_progress and 0 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result


student_1 = Student('Saul', 'Goodman', 'M')
student_1.courses_in_progress += ['Java', 'Python', 'C#']
student_2 = Student('Jesse', 'Pinkman', 'M')
student_2.courses_in_progress += ['Java', 'Python', 'C++']

student_1.finished_courses += ['Java']

mentor_1 = Reviever('Walter', 'White')
mentor_1.courses_attached += ['Java', 'Python']
mentor_2 = Reviever('Gustavo', 'Fring')
mentor_2.courses_attached += ['Java', 'Python']
mentor_3 = Lecturer('Michael', 'Ehrmantraut')
mentor_3.courses_attached += ['Java', 'Python']
mentor_4 = Lecturer('Tuco', 'Salamanca')
mentor_4.courses_attached += ['Java', 'Python']

mentor_1.rate_rev(student_1, 'Python', 9)
mentor_1.rate_rev(student_1, 'Python', 6)
mentor_1.rate_rev(student_2, 'Python', 9)
mentor_1.rate_rev(student_2, 'Python', 10)
mentor_2.rate_rev(student_1, 'Java', 5)
mentor_2.rate_rev(student_1, 'Java', 6)
mentor_2.rate_rev(student_2, 'Java', 6)
mentor_2.rate_rev(student_2, 'Java', 6)

student_1.rate_lect(mentor_3, 'Python', 5)
student_1.rate_lect(mentor_3, 'Python', 8)
student_1.rate_lect(mentor_3, 'Python', 9)
student_1.rate_lect(mentor_3, 'Python', 6)
student_2.rate_lect(mentor_4, 'Java', 9)
student_2.rate_lect(mentor_4, 'Java', 8)
student_2.rate_lect(mentor_4, 'Java', 9)
student_2.rate_lect(mentor_4, 'Java', 10)

students_list = [student_1, student_2]
mentors_list = [mentor_1, mentor_2, mentor_3, mentor_4]

[instance.average_rating() for instance in Student.instance_list_s]
[instance.average_rating() for instance in Lecturer.instance_list_l]


student_1.completion_course('C#')
student_2.completion_course('C++')

print(student_1)
print(student_1.__gt__(student_2))
print(student_1.__eq__(student_2))
print()
print(mentor_4)
print(mentor_3.__gt__(mentor_4))
print(mentor_3.__eq__(mentor_4))
print()
print(mentor_1)
print()


def average_grade_in_subject(class_name, course):
    """
    Средняя оценка по заданным параметрам,
    можно выбрать студентов или лекторов и предмет
    """
    list_instances = [_ for _ in globals().values() if isinstance(_, class_name)]
    list_grades = [_.grades[course] for _ in list_instances if course in _.grades.keys()]
    average_grade = sum([sum(i) for i in list_grades]) / sum([len(i) for i in list_grades])
    return f'Средняя оценка среди {class_name.__name__} по предмету {course} - {average_grade}'


print(average_grade_in_subject(Lecturer, 'Python'))
print(average_grade_in_subject(Student, 'Java'))

