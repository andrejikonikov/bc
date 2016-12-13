class LongRule:
    def __init__(self, arguments, consequent):
        self.arguments = arguments
        self.consequent = consequent
        self.firstFlag = False
        self.secondFlag = False

    def raiseFlag(self, n):
        if n == 1:
            self.firstFlag = True
        else:
            self.secondFlag = True

    def printRule(self):
        for i in range(0, len(self.arguments)):
            if i < len(self.arguments)-1:
                print self.arguments[i], ",",
            else:
                print self.arguments[i], "->", self.consequent,

    def printArguments(self):
        for i in range(0, len(self.arguments)):
            if i < len(self.arguments)-1:
                print self.arguments[i], ",",
            else:
                print self.arguments[i], "."
