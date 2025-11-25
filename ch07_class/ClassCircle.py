class Circle:
    type = '원' # 타입 정의

    def __init__(self, center_x, center_y, radius):
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius
    # end def __init__

    def showinfo(self):
        print('원 중심 : %s, %s' % (self.center_x, self.center_y))
        print('반지름 : %s' % self.radius)

        area = 3.14 * self.radius ** 2
        print('면적 : %s' % area)
    # end def showinfo
# end class Circle


print('도형의 타입 : %s' % (Circle.type))
print('-' * 20)

circle1 = Circle(3, 5, 10)
circle1.showinfo()
print( '-' * 20 )

circle2 = Circle(8, 6, 20)
circle2.showinfo()