print(
    "python", "javascript", sep=" vs ", end="?"
)  # sep은 ,사이에 들어갈거/ end는 마지막에 들어갈거(end기본값은 줄바꿈)
print("무엇이 더 재밌을까요?")  # python vs javascript?무엇이 더 재밌을까요?

import sys

print("python", "javascript", file=sys.stdout)  # 표준출력
print("python", "javascript", file=sys.stderr)  # 표준에러

# 시험성적
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")  # left정렬 8칸, right정렬 4칸

# 은행 대기순번표 001, 002, 003 ...
for num in range(1, 21):
    print("대기번호: " + str(num).zfill(3))  # 3칸인데 없는 자리에는 0을 넣어서 체워라


anser = input("아무 값이나 입력하세요 : ")  # 사용자 형태로 값을 받게되면 항상 문자열로 저장
print("입력하신 값은 " + anser + "입니다.")
