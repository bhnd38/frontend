# students = ['Hermaione', 'Harry', 'Ron']


# for student in students:
#     print(student)

# for i in range(len(students)):
#     print(i+1, students[i])

students = {
    'Hermaione': "Gryffindor",
    'Harry': 'Gryffindor',
    'Ron': 'Gryffindor',
    'Draco': 'Slytherin'
}

for student in students:
    print(student, students[student], sep=': \t ') # value값을 출력하고싶을 때는 딕셔너리[키값] 의 형태로 작성.

