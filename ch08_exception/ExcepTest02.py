# 출석 체크 함수
def checkStudent(name):
    students = ['철수', '영희', '민수', '지영']

    if name in students:
        print(f'학생 \'{name}\'은(는) 출석했습니다.')
    else:
        message = f'학생 \'{name}\'은(는) 명단에 없습니다!'
        raise Exception(message)
# end def checkStudent

try:
    checkList = ['철수', '훈식']

    for student in checkList:
        checkStudent(student)
    # end for

except Exception as err:
    print('예외 발생 : {}'.format(err))
# end try