# 표준 체중을 구하는 프로그램을 작성하시오

# • 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) × 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#     * 함수명 : std_weight
#     * 전달값 : 키(helght), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시


# (출력 예제)
#  키 175cm 남자의 표준 체중은 67.38kg 입니다.


# ## 내 정답
def std_weight(height_cm, gender):
    height_m = height_cm / 100
    if gender == "여자":
        std_weight_f = (height_m * height_m) * 21
        result = round(std_weight_f, 2)
    else:
        std_weight_m = (height_m * height_m) * 22
        result = round(std_weight_m, 2)
    return result

height_cm = 169
gender = "여자"

result = std_weight(height_cm, gender)
print("키 {0}cm {1}의 표준체중은 {2}kg입니다.".format(height_cm, gender, result))



## 강사 정답
def std_weight(height, gender):  # 키 m 단위 (실수), 성별 "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21


height = 175  # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)

print("{0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
