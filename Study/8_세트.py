# 집합 (set)
# 중복 x, 순서 x
my_set = {1, 2, 3, 3, 3}
print(my_set)  # {1, 2, 3}  중복을 허용하지 않기 떄문에

SM = {"카리나", "웬디", "태연"}
aespa = set(["카리나", "윈터"])

# 교집합
print(SM & aespa)
print(SM.intersection(aespa))  # {'카리나'}

# 합집합
print(SM | aespa)
print(SM.union(aespa))  # 집합이라 순서는 상관없음

# 차집합 (애스파가 아닌 에스엠 연예인)
print(SM - aespa)
print(SM.difference(aespa))

# 에스파에 멤버가 추가됨
aespa.add("닝닝")
print(aespa)

# 태연이 소속사를 옮겼어요
SM.remove("태연")
print(SM)
