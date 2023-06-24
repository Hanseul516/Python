import pickle

# 저장하기
profile_file = open("profile.pickle", "wb")  # 쓰기목적으로 바이너리(피클에서 꼭 b를 붙이고 인코당은 안써도 됨)
profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file)  # profile에 있는 정보를 file에 저장
profile_file.close()

# 불러오기
profile_file = open("profile.pickle", "rb")  # 읽기로 불러옴
profile = pickle.load(profile_file)  # file에 있는 정보를 profile에 불러옴
print(profile)
profile_file.close()
