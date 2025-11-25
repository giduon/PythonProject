class Account: # 클래스 정의
    bankname = 'kb' # 클래스 변수

    def __init__(self, name, no, deposit):
        self.name = name
        self.no = no
        self.deposit = deposit
    # end def __init__

    def printData(self):
        print('예금주 : %s' % self.name)
        print('예금주 : %s' % self.no)
        print('예금주 : %s' % self.deposit)
    # end def printData
# end class Account

print('주거래은행 : %s' % Account.bankname)
print('-'*30)

soo = Account('김철수', 1234, 1000) # 객체 생성
soo.printData()
print('-'*30)

hee = Account('박영희', 5678, 2000) # 객체 생성
hee.printData()
