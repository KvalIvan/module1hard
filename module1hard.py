grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
mark = {}
grades_Aaron = sum(grades[0]) / len(grades[0])
grades_Bilbo = sum(grades[1]) / len(grades[1])
grades_Johnny = sum(grades[2]) / len(grades[2])
grades_Khendrik = sum(grades[3]) / len(grades[3])
grades_Steve = sum(grades[4]) / len(grades[4])

# НЕ додумался как сделать иначе чтобы всё было в одной строке, думаю можно как-то, но я могу понять как.
# Если как-то можно, подскажите, буду благодарен!

mark['Aaron'] = grades_Aaron
mark['Bilbo'] = grades_Bilbo
mark['Johnny'] = grades_Johnny
mark['Khendrik'] = grades_Khendrik
mark['Steve'] = grades_Steve

print(mark)