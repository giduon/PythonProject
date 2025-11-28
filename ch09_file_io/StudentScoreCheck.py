# StudentScoreCheck.py
# students.txt 파일을 읽어서 '이름-나이-총점-평균' 형식으로 result2.txt 파일에 기록하는 프로그램

myencoding = 'UTF-8'

# 파일 읽기
source = open(file='students.txt', mode='rt', encoding=myencoding)

# 파일 생성/쓰기
destination = open(file='result2.txt', mode='wt', encoding=myencoding)

# 모든 데이터 줄 읽기
lines = [item.strip() for item in source.readlines()]
print(lines)

for line in lines:
    fields = line.split(',')     # ['홍길동','20','80','90','85']
    print(fields)

    name = fields[0]
    age = int(fields[1])
    kor = float(fields[2])
    eng = float(fields[3])
    math = float(fields[4])

    total = kor + eng + math
    average = total / 3.0

    # 출력 형식: 이름-나이-총점-평균
    result = '%s-%d-%.1f-%.2f\n' % (name, age, total, average)
    print(result)

    destination.write(result)
# end for

source.close()
destination.close()
print('작업이 완료되었습니다.')
