import sqlite3
db = sqlite3.connect("university.db")
cr = db.cursor()
cr.execute("""
    CREATE TABLE IF NOT EXISTS `lecturers`(
        Name TEXT, ID INTEGER, Specializatin Text
        )"""
           )

cr.execute("""
    CREATE TABLE IF NOT EXISTS `courses`(
        Name TEXT, ID TEXT, Credit_Hours INTEGER, Level INTEGER, Is_Compolsary TEXT, Lecturer TEXT
        )"""
           )

cr.execute("""
    CREATE TABLE IF NOT EXISTS `students`(
        Name TEXT, Age INTEGER, ID INTEGER, Level INTEGER, Lecturer TEXT, Course TEXT
        )"""
           )


class Student:
    def __init__(self, name, age, id, level, lecturer, course):
        self.__name = name
        self.__age = age
        self.__id = id
        self.__level = level
        self.__lecturer = lecturer
        self.__course = course

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_level(self):
        return self.__level

    def set_level(self, level):
        self.__level = level

    def get_lecturer(self):
        return self.__lecturer

    def set_lecturer(self, lecturer):
        self.__lecturer = lecturer

    def get_course(self):
        return self.__course

    def set_course(self, course):
        self.__course = course

    def show_details(self):
        return f"Student '{self.get_name()}' Takes '{self.get_course().get_name()}' Which Is Teached By 'Dr.{self.get_course().get_lecturer().get_name()}'"

    def __eq__(self, other):
        return self.get_id() == other.get_id()


class Lecturer:
    def __init__(self, name, id, specialization):
        self.__name = name
        self.__id = id
        self.__specialization = specialization

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_specialization(self):
        return self.__specialization

    def set_specialization(self, specialization):
        self.__specialization = specialization


class Course:
    def __init__(self, name, id, num_of_credit_hours, level, is_compolsary, lecturer):
        self.__name = name
        self.__id = id
        self.__num_of_credit_hours = num_of_credit_hours
        self.__level = level
        self.__is_compolsary = is_compolsary
        self.__lecturer = lecturer

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_num_of_credit_hours(self):
        return self.__num_of_credit_hours

    def set_num_of_credit_hours(self, num_of_credit_hours):
        self.__num_of_credit_hours = num_of_credit_hours

    def get_level(self):
        return self.__level

    def set_level(self, level):
        self.__levle = level

    def get_compolsary_case(self):
        return self.__is_compolsary

    def set_compolsary_case(self, is_compolsary):
        self.__is_compolsary = is_compolsary

    def get_lecturer(self):
        return self.__lecturer

    def set_lecturer(self, lecturer):
        self.__lecturer = lecturer

    def show_details(self):
        return f"'Dr.{self.get_lecturer().get_name()}' Is The Lecturer For '{self.get_name()}'"


def begin():
    # info for lecturer
    print("\nInfo For Lecturer:-")
    name = input("Name: ").title().strip()
    id = int(input("ID: ").strip())
    specialization = input("Specialization: ").title().strip()
    lecturer = Lecturer(name, id, specialization)
    all_data = (name, id, specialization)
    cr.execute("INSERT INTO `lecturers` Values(?, ?, ?)", all_data)

    # info for course
    print("\nInfo For Course:-")
    name = input("Name: ").title().strip()
    id = input("ID: ").upper().strip()
    num_of_credit_hours = int(input("Number Of Credit Hours: ").strip())
    level = int(input("Level: ").strip())
    is_compolsary = input("Is Compolsary: ").title().strip()
    course = Course(name, id, num_of_credit_hours, level, is_compolsary, lecturer)
    lecturer_name = course.get_lecturer().get_name()
    all_data = (name, id, num_of_credit_hours, level, is_compolsary, lecturer_name)
    cr.execute("INSERT INTO `courses` Values(?, ?, ?, ?, ?, ?)", all_data)

    # info for student
    print("\nInfo For Student:-")
    name = input("Name: ").title().strip()
    age = int(input("Age: ").strip())
    id = int(input("ID: ").strip())
    level = int(input("Level: ").strip())
    student = Student(name, age, id, level, lecturer, course)
    all_data = (
        name, age, id, level, student.get_lecturer().get_name(),
        student.get_course().get_name()
    )
    cr.execute("INSERT INTO `students` Values(?, ?, ?, ?, ?, ?)", all_data)
    print(student.show_details())
    print(course.show_details())

    db.commit()
    db.close()


# begin()
std1 = Student("Ali", 18, 20201548, 1, "Mohammed", "Programming 1")
std2 = Student("Zaher", 18, 20200748, 1, "Mohammed", "Programming 1")
print(std1 == std2)
