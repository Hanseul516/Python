python = "Python is Amazing"

print(python.lower())  # 소문자
print(python.upper())  # 대문자
print(python[0].isupper())  # 문자열 맨앞이 대문자니? true
print(len(python))  # 문자열 전체 길이
print(python.replace("Python", "javascript"))  # 문자 Python을 javascript로 바꿔줌.

index = python.index("n")  # "n" 이 몇 번째에 있냐
print(index)
index = python.index("n", index + 1)  # 두 번째 "n"은 몇 번째 있냐
print(index)

print(python.find("n"))  # "n"의 위치를 모두 찾기 떄문에 5,15
print(index)

print(python.find("java"))  # 찾을 수 없으면 -1을 출력
# print(python.index("java"))  # 그냥 에러.
print("hi") # find는 에러없이 -1 출력 후 그냥 진행.

# 찾을 수 없을 때 차이점: index는 에러, find는 -1

print(python.count("n")) # "n"이 총몇번 찍히냐
