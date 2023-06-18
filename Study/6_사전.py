#cabinet
cabinet = {3:"카리나", 100:"윈터"}
print(cabinet[3])
print(cabinet[100])

# cabinet.get()
# print(cabinet[5])  #에러, 즉시 실행종료
print(cabinet.get(5))  #None 출력, 이어서 실행
print(cabinet.get(5, "사용가능"))  #5를 가져오려고 시도, 값이 없으면 "사용가능을 가져옴"
print("hi")

# in
print(3 in cabinet)  # 3이 cabinet안에 있으면 True
print(5 in cabinet)  # 없으면 False

#str도 가능
cabinet = {"A-3":"카리나", "B-100":"윈터"} 
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["A-3"] = "닝닝"  # "A-3"자리에 카리나대신 닝닝이 들어감
cabinet["B-10"] = "지젤"  # 지젤이 추가
print(cabinet)  # {'A-3': '닝닝', 'B-100': '윈터', 'B-10': '지젤'}

# 손님 감(del)
del cabinet["A-3"]  # "A-3" 삭제
print(cabinet) # {'B-100': '윈터', 'B-10': '지젤'}

#key들만 출력
print(cabinet.keys()) #dict_keys(['B-100', 'B-10'])

#value들만 출력
print(cabinet.values()) #dict_values(['윈터', '지젤'])

# key, value 쌍으로 출력
print(cabinet.items()) #dict_items([('B-100', '윈터'), ('B-10', '지젤')])

# 목욕탕 폐점
cabinet.clear()
print(cabinet)  #{}