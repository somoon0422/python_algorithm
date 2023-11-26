import random as rd
import sortMod as sm

students = []

for i in range(20):
    students.append(rd.randint(170,185))
print(f'students: {students}')

sortedStudents = sm.bubbleSort(students)
print(f'students: {students}')
print(f'sortedStudents: {sortedStudents}')
