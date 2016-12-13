class Rule:
    def __init__(self, firstLeft, secondLeft, consequent):
        self.firstLeft = firstLeft
        self.secondLeft = secondLeft
        self.consequent = consequent
        self.firstFlag = False
        self.secondFlag = False

    def raiseFlag(self, n):
        if n == 1:
            self.firstFlag = True
        else:
            self.secondFlag = True

    def printRule(self):
        if self.secondLeft == False:
            print self.firstLeft, '->', self.consequent,
        else :
            print self.firstLeft, ',', self.secondLeft, '->', self.consequent,
