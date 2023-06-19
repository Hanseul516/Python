def open_account():
    print("계좌가 생성되었습니다.")


def deposit(balance, money):  # 입금 함수
    print("입금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance + money))
    return balance + money  # 잔액 + 입금금액


def withdraw(balance, money):  # 출금 함수
    if balance >= money:
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 불가합니다. 잔액은 {0}원입니다.".format(balance))
        return balance


def withdraw_night(balance, money):
    commission = 100
    return commission, balance - money - commission


balance = 15000  # 잔액이 0
commission, balance = withdraw_night(balance, 10000)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))
