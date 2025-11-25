# ExcepTest01.py

try:
    su1 = 10
    su2 = '20'

    result = su1 + su2
    print('예외가 발생하지 않았으므로, 이 부분은 실행이 됩니다.')
    print(result)

except Exception as err:
    print('기타 나머지 예외 발생.')
    print('예외 객체 정보 : %s' % err)
# end try



try:
    mydict = {'hong': 10, 'kim': 20}
    findKey = 'choi'
    print('예외가 발생하지 않았으므로, 이 부분은 실행이 됩니다.')
    print(mydict[findKey])

except Exception as err:
    print('기타 나머지 예외 발생.')
    print('예외 객체 정보 : %s' % err)
# end try