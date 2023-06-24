score_file = open("score.txt", "w", encoding="utf8")  # score.txt의 이름을 가진 파일을 쓰기목적으로 열어서
print("수학: 0", file=score_file)  # 이 내용을 파일에 쓰고
print("영어: 50", file=score_file)
score_file.close()  # 파일을 닫는다

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학: 80")
score_file.write("\n코딩: 100")  # write는 줄바꿈이 안돼서 \n써줌
score_file.close()

# score.txt 내용
# 수학: 0
# 영어: 50
# 과학: 80
# 코딩: 100

# 파일을 불러오기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())  # 모든 파일내용을 불러옴
score_file.close()

# 한줄한중 불러오기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline())  # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())  # 줄바꿈을 안하고 싶으면 , end="" 를 추가
print(score_file.readline())
print(score_file.readline())
score_file.close()

# 파일이 몇줄일지 모를때(다른사람파일)
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")  # 줄바꿈 안하려면 , end="" 를 추가
score_file.close()

# 리스트로 불러오기
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # 모든 줄을 list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
