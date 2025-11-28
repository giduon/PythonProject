class MinJumsuException(Exception):
    def __init__(self, message):
        super().__init__(message)
# end class MinJumsuException

class FailedException(Exception):
    def __init__(self, message):
        super().__init__(message)
# end class FailedException

try:
    name = input('이름 입력 : ')
    kor = int(input('국어 점수 입력 : '))
    eng = int(input('영어 점수 입력 : '))
    math = int(input('수학 점수 입력 : '))

    if kor < 40 or eng < 40 or math < 40:
        msg = '%s님 과락입니다.' % name
        # 객체 생성 후 raise 실행
        raise MinJumsuException(msg)

    average = (kor + eng + math) / 3.0
    if average < 60.0:
        msg = '%s님 불합격입니다.' % name
        raise FailedException(msg)

    print('%s님 합격입니다.' % name)

except MinJumsuException as err:
    print('시험을 잘못 보셨군요.')
    print(err)

except FailedException as err:
    print('조금만 더 공부하시길 바랍니다.')
    print(err)

except Exception as err:
    print('기타 예외 발생.')
    print(err)
# end try