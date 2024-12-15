grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades_average = [sum(grades[0]) / len(grades[0]), # Подсчет среднего балла
sum(grades[1]) / len(grades[1]),
sum(grades[2]) / len(grades[2]),
sum(grades[3]) / len(grades[3]),
sum(grades[4]) / len(grades[4])]
list_1 = list(students)
list_1.sort()
average_score_of_each = dict(zip(list_1, grades_average))
print(average_score_of_each)











