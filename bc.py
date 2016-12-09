from fileHandler import getData
print "import done"
newFacts = []
walked = []
road = []

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

def printFacts(s, f):
    print s,
    for i in range(0, len(f)):
        if i < len(f)-1:
            print f[i], ",",
        else:
            print f[i], ".",

def printRules(r):
    for i in range(0, len(r)):
        print "      R", i+1, ":",
        r[i].printRule()
        print

def checkTerminal(facts, target):
    if target in facts:
        return True
    else:
        return False


def dontHaveSuitableRule(target):
    global rules
    # print "searching for :", target
    for r in rules:
        if r.consequent == target:
            # r.printRule()
            # print r.consequent, target
            return False
    return True

def printDots():
    global iteration
    global numberOfDots

    print "   ", iteration,")",
    for i in range(0, numberOfDots):
        print ".",

def printRoad():
    global road
    printRules(road)



def algorythm(target):
    global numberOfDots
    global iteration
    global newFacts
    global walked

    numberOfDots += 1
    iteration += 1

    if (target in facts):
        printDots()
        print "Tikslas ", target,
        printFacts(". Faktas (duotas), nes faktai ", facts)
        return True
    elif (target in newFacts):
        printDots()
        print "Tikslas ", target,
        printFacts(". Faktas (buvo gautas), nes faktai ", facts),
        printFacts(" ir ", newFacts), "."
        return True
    elif dontHaveSuitableRule(target):
        printDots()
        # printRules(rules)
        print "Tikslas ", target, ". Nera taisykliu jo isvedimui. Griztame, FAIL."
        return False
    for rule in rules:
        if (target in walked):
            printDots()
            print"Tikslas ", target, ". Ciklas. Griztame, FAIL."
            return False
        elif (rule.consequent == target):
            isUsable = True
            printDots()
            print "Tikslas ", target, ". Randame ",
            rule.printRule()
            print ". Nauji tikslai ", rule.firstLeft, rule.secondLeft, "."
            walked.append(target)
            arguments = []
            arguments.append(rule.firstLeft)
            if rule.secondLeft != False:
                arguments.append(rule.secondLeft)
            for a in arguments:
                if not algorythm(a):
                    isUsable = False
                    break
                if not(a == rule.firstLeft):
                    print
                else:
                    print"Griztame, sekme."
                numberOfDots -= 1
            if isUsable:
                newFacts.append(rule.consequent)
                road.append(rule)
                iteration += 1
                printDots()
                print "Tikslas ", target,
                printFacts(". Faktas (dabar gautas). Faktai ", facts),
                printFacts(" ir ", newFacts), "."
                walked.pop()
                return True
            else:
                if len(road) != 0:
                    road.pop()
                iteration += 1
                numberOfDots -= 1
                if target in walked:
                    walked.pop()
                # printFacts("a", newFacts)
                newFacts = []
                # printFacts("aa", newFacts)

    printDots()
    print "Tikslas ", target, ". Nera daugiau taisykliu jo isvedimui. Griztame, FAIL."
    return False









# main actions -\/-
fileNames = ["bTest1.txt"]
print fileNames

for fileName in fileNames:
    data = getData(fileName)
    # print data

    importedRules = data[0]
    importedFacts = data[1]
    importedTarget = data[2]

    # init rules
    rules = []
    for i in range(0, len(importedRules)):
        currentRule = importedRules[i]
        if len(currentRule) == 3:
            rules.append(Rule(currentRule[2], False, currentRule[0]))
        else:
            rules.append(Rule(currentRule[2], currentRule[4], currentRule[0]))

    # init facts
    facts = []
    temp = importedFacts[0].replace(" ", "")
    for i in range(0, len(temp)):
        facts.append(temp[i])

    # init target
    target = importedTarget[0]
    # init section --END--

    print "1 DALIS. Duomenys"
    print
    print "   1) Taisykles"
    printRules(rules)
    print
    print "   2) Faktai"
    printFacts("      ", facts)
    print
    print "   3) Tikslas"
    print "      ",target
    print
    path = []

    numberOfDots = 0
    iteration = 0
    newFacts = []

    if checkTerminal(facts, target):
        print "3 DALIS. Rezultatai"
        message = "   1) Tikslas tarp faktu."
        print message
    else:
        print "2 DALIS. Vykdymas"
        print

        if algorythm(target):
            print " Griztame, sekme.\n\n3 DALIS. Rezultatai"
            print " 1) Tikslas ", target, " isvestas."
            print " 2) Kelias: "
            if len(road) == 0:
                print "tuscias."
            else:
                printRoad();

        else:
            print "\n3 DALIS. Rezultatai"
            print " 1) Tikslas ", target, ". Kelias neegzistuoja."


































print "the end"
