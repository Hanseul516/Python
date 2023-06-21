# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름: {0}\t나이: {1}\t".format(name, age), end="") #end를 ''로 설정하면 줄바꿈 없이 연속해서 출력가능
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):  #서로다른 개수의 값을 넣어줄때 *가변인자 사용
    print("이름: {0}\t나이: {1}\t".format(name, age), end="") #end를 ''로 설정하면 줄바꿈 없이 연속해서 출력가능
    for lang in language:
        print(lang, end="")

profile("SM", 00, "엑소", "샤이니", "소녀시대", "레드벨벳", "엔시티")
profile("YG", 10, "빅뱅", "투애니원")
