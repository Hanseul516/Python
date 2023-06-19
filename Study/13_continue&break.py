absent = [2,5]  #결석
no_book = [7]  #책을 안가져옴

for student in range(1,11):  #1~10
    if student in absent:
        continue  #student 안에 absent가 포함되면 아래 문장 실행 안하고 반복묵 계속 실행.
    elif student in no_book:
        print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(student))
        break  # 뒤에 반복문이 있어도 그냥 반복문을 탈출
    print("{0}, 책을 읽어봐".format(student))