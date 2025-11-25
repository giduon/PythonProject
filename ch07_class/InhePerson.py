class Person:
    # 일반화 : 공통된 변수는 수퍼클래스에 작성
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    # end def __init__

    def showData(self):
        print('이름 : ' + str(self.name))
        print('성별 : ' + str(self.gender))
        print('나이 : ' + str(self.age))
    # end def showData
# end class Person

class Employee(Person): # 서브 클래스(수퍼클래스)
    def __init__(self, name, age, gender, salary, hiredate ):
        super().__init__(name, age, gender)
        self.salary = salary
        self.hiredate = hiredate
    # end def __init__

    def getName(self):
        return self.name + '님'
    # end def getName

    def showData(self):
        super().showData()
        print('급여 : ' + str(self.salary))
        print('입사 일자 : ' + str(self.hiredate))
    # end def showData

    def doWork(self):
        print(super().name + '열심히 일합니다.')
    # end def doWork
# end class Employee

class Student(Person):
    pass
# end class Student

soo = Employee('김철수', 20, '남자', 50000, '2020/12/25')
soo.showData()
soo.doWork()
print('-'*30)

# hee = Student('박영희', 19, '여자', '국어', 'A학점')
# print('-'*30)
