# 출석번호가 1,2,3,4. 앞에 100을 붙이기로함. -> 101, 102, 103, 104.
students = [1,2,3,4]
students = [i+100 for i in students]
print(students) #[101, 102, 103, 104]

# 학생이름을 길이로 변환
students = ["karina", "winter", "ningning"]
students = [len(i) for i in students]
print(students)  #[6, 6, 8]

# 학생이름을 대문자로 변환
students = ["karina", "winter", "ningning"]
students = [i.upper() for i in students]
print(students)  #['KARINA', 'WINTER', 'NINGNING']

