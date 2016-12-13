from fileHandler import getData
# from Rule import Rule
from longRule import LongRule
from laborer import printFacts
from laborer import printRules
from laborer import checkTerminal
from laborer import askForInput

print "import done"
newFacts = []
walked = []
path = []

def dontHaveSuitableRule(target):
    global rules
    for r in rules:
        if r.consequent == target:
            return False
    return True

def printPoints():
    global iteration
    global numberOfDots
    print "   ", iteration,")",
    for i in range(0, numberOfDots):
        print ".",

def printPath():
    global path
    for n in range(0, len(path)):
        temp = path[n]
        if n < len(path) - 1 :
            print temp[0],",",
        else:
            print temp[0],"."

def bc(target): # 1. Pradedame naujo tikslo paieska.
    global numberOfDots
    global iteration
    global newFacts
    global walked

    numberOfDots += 1
    iteration += 1
    # 2. Patikriname, ar tikslas yra tarp duotu faktu, jei taip - graziname True.
    if (target in facts):
        printPoints()
        print "Tikslas ", target,
        printFacts(". Faktas (duotas), nes faktai ", facts)
        return True
    # 3. Patikriname, ar tikslas yra tarp gautu faktu, jei taip - graziname True.
    elif (target in newFacts):
        printPoints()
        print "Tikslas ", target,
        printFacts(". Faktas (buvo gautas), nes faktai ", facts),
        printFacts(" ir ", newFacts), "."
        return True
    # 4. Patikriname, ar yra taisykle, kurios desineje puseje yra musu tikslas.
    elif dontHaveSuitableRule(target):
        printPoints()
        print "Tikslas ", target, ". Nera taisykliu jo isvedimui. Griztame, FAIL."
        return False
    i = 0
    # 5. Patikriname visas taisykles, kurios turi desineje puseje tiksla.
    # Jei taisykles buvo visos perziuretos, tai graziname False.
    for rule in rules:
        i += 1
        # 6. Neperziuretai taisyklei patikriname,
        # ar taisykle nebuvo panaudota anksciau (kad nesusidarytu ciklas)
        if (target in walked):
            printPoints()
            print"Tikslas ", target, ". Ciklas. Griztame, FAIL."
            return False
        elif (rule.consequent == target):
            isUsable = True
            printPoints()
            print "Tikslas ", target, ". Randame R",i,":",
            rule.printRule()
            print ". Nauji tikslai ",
            rule.printArguments()
            walked.append(target)
            # 7. Atrinkus taisykle, pagal ankstesniose punktose aprasytas salygas,
            # kiekvienam taisykles, kairiosios puses faktui,
            # pradedame algoritma nuo (1) zingsnio.
            for a in rule.arguments:
                if not bc(a): # Jei bent vienas algoritmo kvietimas grazina False
                # - griztame i (5) zingsni
                    isUsable = False
                    break
                position = len(rule.arguments) - 1
                if not(a == rule.arguments[position]):
                    print
                else:
                    print"Griztame, sekme."
                numberOfDots -= 1
            if isUsable:
                newFacts.append(rule.consequent)
                pair = ["R"+`i` ,  rule]
                path.append(pair)
                iteration += 1
                printPoints()
                print "Tikslas ", target,
                printFacts(". Faktas (dabar gautas). Faktai ", facts),
                printFacts(" ir ", newFacts), "."
                walked.pop()
                return True
            else:
                if len(path) != 0:
                    path.pop()
                iteration += 1
                numberOfDots -= 1
                if target in walked:
                    walked.pop()
                newFacts = []

    printPoints()
    print "Tikslas ", target, ". Nera daugiau taisykliu jo isvedimui. Griztame, FAIL."
    return False

# main actions -\/-
fileNames = ["../tests/bTest1.txt", "../tests/bTest2.txt", "../tests/bTest3.txt", "../tests/bTest4.txt", "../tests/bTest5.txt", "../tests/bTest6.txt", "../tests/bTest7.txt", "../tests/bTest8.txt", "../tests/bTest9.txt", "../tests/bTest10.txt"]
print fileNames

for fileName in fileNames:
    if askForInput(fileName):
        data = getData(fileName)

        importedRules = data[0]
        importedFacts = data[1]
        importedTarget = data[2]

        # init rules
        rules = []
        for i in range(0, len(importedRules)):
            currentRule = importedRules[i]
            cons = False
            args = []
            for i in range(0, len(currentRule)):
                if i%2 == 0:
                    if i == 0:
                        cons = currentRule[i]
                    elif i > 0:
                        args.append(currentRule[i])

            rules.append(LongRule(args, cons))

        # init facts
        facts = []
        temp = importedFacts[0].replace(" ", "")
        for i in range(0, len(temp)):
            facts.append(temp[i])

        # init target
        target = importedTarget[0]

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

            if bc(target):
                print " Griztame, sekme.\n\n3 DALIS. Rezultatai"
                print " 1) Tikslas ", target, " isvestas."
                print " 2) Kelias: ",
                if len(path) == 0:
                    print "tuscias."
                else:
                    printPath();
                print

            else:
                print "\n3 DALIS. Rezultatai"
                print " 1) Tikslas ", target, ". Kelias neegzistuoja."




print "the end"
