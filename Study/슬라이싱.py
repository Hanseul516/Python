# 슬라이싱

jumin = "000516-1234567"

print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) # 0 ~ 2 '직전'까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[0:6])
print("주민번호 뒷자리 : " + jumin[7:])
print("주민번호 뒷자리 뒤에서부터 : "+ jumin[-7:])