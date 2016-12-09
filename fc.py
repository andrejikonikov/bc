from fileHandler import getData

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
            print f[i], "."

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

def askForInput(param):
    print "want to run ", param, "?(yes/no)"
    yes = set(['yes','y', 'ye', ''])
    no = set(['no','n'])
    choice = raw_input().lower()
    if choice in yes:
        return True
    elif choice in no:
        return False
    else:
        print "Please respond with 'yes' or 'no'"

def printPath(p):
    for pp in p:
        print pp,





def doFC(filename):
    # init section --
    data = getData(filename)
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

    if checkTerminal(facts, target):
        print "3 DALIS. Rezultatai"
        message = "   1) Tikslas tarp faktu."
        print message
    else:
        print "2 DALIS. Vykdymas"
        print
        iterations = 0
        usedRules = 1
        message = ""

        while (iterations < len(rules))  and  (usedRules <= len(rules)):
            if checkTerminal(facts, target):
                message = "Tikslas gautas."
                break
            if usedRules == len(rules):
                message = "kelias neegzistuoja."
                break
            print
            print "   ",iterations + 1,"iteracija"

            for i in range(0, len(rules)):
                r = rules[i]

                if r.firstFlag:
                    print "      R",i,": ",
                    r.printRule()
                    print "praleidziame nes pakelta flag1."
                elif r.secondFlag:
                    print "      R",i,": ",
                    r.printRule()
                    print "praleidziame nes pakelta flag2."
                elif r.firstLeft not in facts:
                    print "      R",i,": ",
                    r.printRule()
                    print "netaikome, nes truksta", r.firstLeft

                elif (r.secondLeft != False) and (r.secondLeft not in facts):
                    if (r.secondLeft not in facts):
                        print "      R",i,": ",
                        r.printRule()
                        print "netaikome, nes truksta", r.secondLeft

                elif r.consequent in facts:
                    r.raiseFlag(2)
                    print "      R",i+1,": ",
                    r.printRule()
                    print "netaikome, nes konsekventas faktuose. Pakeliame flag2."
                else:
                    facts.append(r.consequent)
                    r.raiseFlag(1)
                    print "      R",i,": ",
                    st = "R" + `i+1`
                    path.append(st)
                    r.printRule()
                    print "taikome. Pakeliame flag1.",
                    printFacts(" Faktai", facts)
                    iterations += 1
                    usedRules += 1
                    break
        print "3 DALIS. Rezultatai"
        print "   1) ", message
        if ((message != "kelias neegzistuoja.") and (len(path) > 0)):
            print "   2) ",
            printPath(path)

filenames = ["test1.txt", "test2.txt", "test3.txt", "test4.txt", "test5.txt" ]

for fn in filenames:
    if askForInput(fn):
        print doFC(fn)



print "done"
