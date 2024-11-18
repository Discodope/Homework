grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

sorted_students = sorted(students)

import statistics
average_grades = [statistics.mean(sublist) for sublist in grades]

students_grades = dict(zip(sorted_students, average_grades))
print(students_grades)