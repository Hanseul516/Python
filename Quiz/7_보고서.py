# 회사에서 매주 1회 작성해야하는 보고서가 있다.
# 보고서는 항상 같은 형태로 만들어야 한다.

# - X 주차 주간보고 =
# 부서 :
# 이름 :
# 업무 요약 :

# 1주차부터 50주차까지의 보고서파일을 만드는 프로그램을 작성하시오.
# 조건 : 파일명은 '1주차.txt', '2주차.txt', ...


# 내가 만든 답
for i in list(range(1, 51)):
    with open(f"{i}주차.txt", "w", encoding="utf8") as weekly_file:
        weekly_file.write(
            """- {0} 주차 주간보고 =
부서 :
이름 :
업무 요약 :""".format(
                i
            )
        )

# 강사님 답
for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약 :")
