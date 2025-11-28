myencoding = 'UTF-8'

source = open(file='jumsu.txt', mode='rt', encoding=myencoding) # 읽어올 파일
destination = open(file='result.txt', mode='wt', encoding=myencoding) # 신규 생성할 파일

data = [item.strip() for item in source.readlines()]
print(data)

for bean in data:
    # print(type(bean))
    human = bean.split(',')
    # print(human)
    name = human[0]
    kor = float(human[1])
    eng = float(human[2])
    math = float(human[3])
    _gender = human[4].upper() # lower() 함수도 참고

    total = kor + eng + math
    average = total/3.0

    if _gender == 'M':
        gender = '남자'
    else:
        gender = '여자'
    # end if

    # 표시 형식 : '이름/성별/총점/평균'
    sentences = '%s/%s/%.1f/%.2f\n' % (name, gender, total, average)
    print(sentences, file=destination)
    destination.write(sentences)
# end for

source.close()
destination.close()

print('처리 작업이 완료 되었습니다.')
