grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_sortd = sorted(list(students))
print(students_sortd)
print(type(students_sortd))
a = sum(grades[0]) / len(grades[0])
b = sum(grades[1]) / len(grades[1])
j = sum(grades[2]) / len(grades[2])
k = sum(grades[3]) / len(grades[3])
s = sum(grades[4]) / len(grades[4])

resalt = {students_sortd[0]: a,
         students_sortd[1]: b,
         students_sortd[2]: j,
         students_sortd[3]: k,
         students_sortd[4]: s}
print(resalt)