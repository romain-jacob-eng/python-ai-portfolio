# Project 1 — Student Grade Analyzer
# Analyzes student grades using OOP, calculates averages and displays a bar chart.

import matplotlib.pyplot as plt


class Student:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        try:
            return sum(self.grades) / len(self.grades)
        except ZeroDivisionError:
            return 0


class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def show_results(self):
        for student in self.students:
            print(f"{student.first_name}: {student.average():.1f}")

    def plot_results(self):
        names = [s.first_name for s in self.students]
        averages = [s.average() for s in self.students]
        plt.bar(names, averages, color="steelblue")
        plt.ylim(0, 20)
        plt.title("Class Results")
        plt.xlabel("Students")
        plt.ylabel("Average")
        plt.show()


if __name__ == "__main__":
    romain = Student("Romain", 19)
    romain.add_grade(17)
    romain.add_grade(17)
    romain.add_grade(14)

    camille = Student("Camille", 21)
    camille.add_grade(18)
    camille.add_grade(20)
    camille.add_grade(17)

    pierre = Student("Pierre", 17)
    pierre.add_grade(12)
    pierre.add_grade(7)
    pierre.add_grade(8)

    classroom = Classroom()
    classroom.add_student(romain)
    classroom.add_student(camille)
    classroom.add_student(pierre)

    classroom.show_results()
    classroom.plot_results()