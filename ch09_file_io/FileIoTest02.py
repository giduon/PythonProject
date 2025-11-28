filename = 'coffee_list.txt'
myencoding = 'UTF-8'

print('readline() 함수는 1줄을 읽어 옵니다.')
myfile01 = open(file=filename, mode='rt', encoding=myencoding)
while True:
    oneline = myfile01.readline().strip()

    # 파이썬에서 empty한 데이터는 부정(False)으로 취급
    if not oneline:
        print(type(oneline))
        print('[' + oneline + ']')
        break
    print('[' + oneline + ']')

myfile01.close()

print('\nreadlines() 함수는 모든 줄을 읽어서 list로 반환해 줍니다.')
myfile02 = open(file=filename, mode='rt', encoding=myencoding)
coffee_list = [txt.strip() for txt in myfile02.readlines()]
print(coffee_list)
myfile02.close()

print('\nread() 함수는 파일 내용 전체를 문자열로 반환해 줍니다.')
myfile03 = open(file=filename, mode='rt', encoding=myencoding)
coffee_text = myfile03.read()
print(type(coffee_text))
print(coffee_text)
myfile03.close()
