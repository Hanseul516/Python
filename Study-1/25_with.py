# import pickle

# with open("profile.pickle", "rb") as profile_file:  # 파일을 열어서 profile_file 변수에 저장
#     print(pickle.load(profile_file))  # 파일내용을 피클로드로 불러와서 출력함
#     # close 할필요없이 with문을 탈출하면서 자동으로 종료됨


# 피클을 사용하지 않고 일반적인 파일을 쓰고 읽는거를 with를 활용해서 2줄만에 완~
with open(
    "study.txt", "w", encoding="utf8"
) as study_file:  # 파일을 작성해서(w) study_file 변수에 저장
    study_file.write("파이썬을 열심히 공부하고 있어요.")  # 파일을 작성함

with open(
    "study.txt", "r", encoding="utf8"
) as study_file:  # 읽기모드로 파일을 불러와서 study_file에 저장
    print(study_file.read())
