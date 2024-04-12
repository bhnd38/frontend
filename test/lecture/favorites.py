import csv

from cs50 import SQL

db = SQL('sqlite:///favorites.db') #'sqlite:///server ip: port/favorites.db'

language = input("Favorite language: ")

rows = db.execute("Select language, count(*) as n from favorites group by ?", language) # ?의 위치에 뒤에 지정한 변수값 language가 온다
# rows = db.execute(f"Select count(*) as n from favorites where problem like {language}")
# 위와 같이 작성해도 실행은 되나 보안에 취약하다는 약점이 있다. 밑에 상세 설명 참조.

print(rows)

row = rows[0]

print(row['n'])



# # file = open("favorites.csv" , "r") # 이런 방법으로도 파일을 열 수 있다.
# # reader = csv.reader(file)
# # next(reader)
# # for row in reader:
# #     print(row[1])

# # file.close() # 그러나 이 방법은 이처럼 파일을 직접 닫아줘야한다.

# with open("favorites.csv", 'r') as file: # with as로 여는 방법은 with문이 끝나면 자동으로 파일을 닫아준다.
#     reader = csv.DictReader(file) # csv.reader()는 데이터를 리스트의 형태로 불러온다. # 딕셔너리 형태로 불러오고 싶을 땐 csv.DicReader()

#     count = {}


#     for row in reader:
#         language=row["language"]
#         if language in count:
#             count[language] += 1
#         else:
#             count[language] = 1

# for language in sorted(count, reverse=True):
#     print(f"{language}: {count[language]}")





# ---------------------------------
# BEGIN TRANSACTION
# COMMIT
# ROLLBACK
# -> transaction problem: 한쪽에선 데이터를 보냈는데 반대쪽에선 데이터를 받지 못하는 경우의 문제.
# 이를 방지하기 위한 시스템.

'''
f string의 보안상 취약점
ex)
로그인 프로그램일 때,
ID는 harvard@edu 일때, 로그인 시 harvard@edu'-- 라고 적어버리면

rows = db.execute(f'Select from users where username = {} AND password = {}')
에서
rows = db.execute(f'Select from users where username = 'harvard@edu'--' AND password = {}')
가 되어버려서 password 부분이 따옴표 안에 들어가버려 무시된 채 다음으로 진행된다.
password를 입력하지 않고도 로그인하게 되는 경우 발생.
'''
