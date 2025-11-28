class Sports:
    def __init__(self, name, entry ):
        self.name = name
        self.entry = entry
                  
    def showData(self):
        print('종목 : %s' % ( self.name ))    
        print('엔트리 : %2d명' % ( self.entry ))
# end class Sports
 
class BaseBall(Sports):
    def __init__(self, name, entry, hitrate):
        super().__init__(name, entry)
        self.hitrate = hitrate

    def showData(self):
        super().showData() 
        print('타율  : %f' % ( self.hitrate ))
# end class BaseBall

 
class FootBall(Sports):
    def __init__(self, name, entry, goal):
        super().__init__(name, entry)
        self.goal = goal
        
    def showData(self):
        super().showData() 
        print('골수  : %d' % ( self.goal ))    
# end class FootBall
 
base = BaseBall('야구', 9, 0.235)
base.showData()
print('-' * 20)
foot = FootBall('축구', 11, 5)
foot.showData()
print('-' * 30)