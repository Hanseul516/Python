# 리스트

#지하철 칸별로 10명, 20명, 30명
#subway1 = 10
#subway2 = 20
#subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["카리나", "윈터", "지젤"]
print(subway)

#윈터가 몇 번째 칸에 타고 있는가?
print(subway.index("윈터"))

#다음 정류장에 닝닝이 다음 칸에 탐
print(subway.append("닝닝"))  # append는 맨뒤에 붙게 함

# 태연을 카리나/윈터 사이에 태우기
subway.insert(1, "태연")
print(subway)

# 뒤에서 부터 한명씩 꺼냄
print(subway.pop())  #닝닝
print(subway)  #['카리나', '태연', '윈터', '지젤']

# 동명이인이 몇명 있는지 알아보기
subway.append("윈터")
print(subway.count("윈터"))

#정렬도 가능
num_list = [5,3,4,2,1]
num_list.sort()
print(num_list)

#순서 뒤집기 가능
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용 가능
num_list = [5,3,4,2,1]
mix_list = ["카리나", 24, True]
print(mix_list)

#리스트 합침
num_list.extend(mix_list)
print(num_list)