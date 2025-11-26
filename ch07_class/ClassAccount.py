class Account: # 클래스 정의
    bankname = 'KB' # 클래스 변수

    def __init__(self, name, no, deposit):
        # 인스턴스 변수 : self 키워드를 사용하여 선언한 변수
        self.name = name
        self.no = no
        self.deposit = deposit
    # end def __init__

    def input(self, money):
        print('%s님 계좌에 %d원 입금' % (self.name, money))
        self.deposit += money
    # end def input

    def output(self, money):
        print('%s님 계좌에서 %d원 출금' % (self.name, money))
        self.deposit -= money
    # end def output

    def printData(self):
        print('예금주 : %s' % self.name)
        print('계좌 번호 : %d' % self.no)
        print('예치금 : %d' % self.deposit)
    # end def printData
# end class Account

print('주거래은행 : %s' % Account.bankname)
print('-'*30)

soo = Account('김철수', 1234, 1000) # 객체 생성

soo.input(2000)

soo.printData()
print('-'*30)

hee = Account('박영희', 5678, 2000)
hee.output(500)
hee.printData()

# 매우 “동적(dynamic)”인 언어
hee.bankname = '국민 은행' # 영희 객체에 bankname 인스턴스 변수가 생김

print('주거래은행 : %s' % Account.bankname)