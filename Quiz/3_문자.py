# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com

# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 +'글자 갯수 + 글자 내 'e• 갯수 + "!" 로 구성
#                 (nav)         (5)         (1)         (!)

# 예) 생성된 비밀번호 : nav51!

naver ="http://naver.com"

front_naver = naver.replace("http://", "")
back_naver = front_naver.replace(".com", "")

password = back_naver[:3] + str(len(back_naver)) + str(back_naver.count("e")) + "!"

print(password)  # nav51!