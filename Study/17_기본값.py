# def profile(name, age, main_lang):
#     print("이름 :{0}\t나이 : {1}\t언어: {2}".format(name, age, main_lang))

# profile("카리나", 23, "한국어")
# profile("닝닝", 21, "중국어")

# 같은 학교 같은 학년 같은 반 같은 수업.


def profile(name, age=19, main_lang="한국어"):
    print("이름 :{0}\t나이 : {1}\t언어: {2}".format(name, age, main_lang))

profile("카리나")  # 나이랑 언어가 기본값으로 지정됨.
profile("윈터")