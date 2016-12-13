from fileHandler import getData
from laborer import printFacts
from laborer import printRules
from laborer import checkTerminal
from laborer import askForInput
from Rule import Rule

def printPath(p):
    for pp in p:
        print pp,

# 1.Isvedimo paieska pradedama nuo pradiniu faktu, produkciju ir tikslo.
def doFC(rules, facts, target):
    if checkTerminal(facts, target):
        print "3 DALIS. Rezultatai"
        message = "   1) Tikslas tarp faktu."
        print message
    else:
        print "2 DALIS. Vykdymas"
        iterations = 0
        usedRules = 1
        message = ""
        # 2.kol taisykliu sarase yra taisykle, kuria galima pritaikyti
        # turimiems faktams, perrenkama nauja iteracija.
        while (iterations < len(rules))  and  (usedRules <= len(rules)):
            if checkTerminal(facts, target):
                # 8.Sekme - ieskoma produkciju seka egzistuoja, algoritmas baigia darba.
                message = "Tikslas gautas."
                break
            # 10.Jei liko neperziuretu produkciju, griztame i 3 zingsni,
            # jei produkcijos perziuretos, tai nesekme - ieskoma
            # produkciju seka neegzistuoja, algoritmas baigia darba.
            if usedRules == len(rules):
                message = "kelias neegzistuoja."
                break
            # 9.Valdymas perduodamas sekanciai iteracijai (griztame i 2 zingsni).
            print
            print "   ",iterations + 1,"iteracija"
            # 3.Visos turimos taisykles perrenkamos is eiles.
            for i in range(0, len(rules)):
                r = rules[i]
                if r.firstFlag:
                    print "      R",i+1,": ",
                    r.printRule()
                    print "praleidziame nes pakelta flag1."
                elif r.secondFlag:
                    print "      R",i+1,": ",
                    r.printRule()
                    print "praleidziame nes pakelta flag2."
                elif r.firstLeft not in facts:
                    print "      R",i+1,": ",
                    r.printRule()
                    print "netaikome, nes truksta", r.firstLeft
                elif (r.secondLeft != False) and (r.secondLeft not in facts):
                    if (r.secondLeft not in facts):
                        print "      R",i+1,": ",
                        r.printRule()
                        print "netaikome, nes truksta", r.secondLeft
                elif r.consequent in facts:
                    r.raiseFlag(2)
                    print "      R",i+1,": ",
                    r.printRule()
                    print "netaikome, nes konsekventas faktuose. Pakeliame flag2."
                # 4.Jeigu paimta produkcija galime taikyti, pereiname i 5 zingsni,
                #kitu atveju i 10.
                else:
                    # 5.pakeliame flag1, pereiname i 6 zingsni.
                    r.raiseFlag(1)
                    # 6.isimename taisykles tiksla, kaip fakta, ir pereiname i 7 zingsni.
                    facts.append(r.consequent)
                    print "      R",i+1,": ",
                    st = "R" + `i+1`
                    path.append(st)
                    r.printRule()
                    print "taikome. Pakeliame flag1.",
                    printFacts(" Faktai", facts)
                    print
                    iterations += 1
                    usedRules += 1
                    break
                    # 7.Jei po produkcijos pritaikymo gaunama terminaline busena,
                    # tai pereiti i 8 zingsni, jei ne, eiti i 9.
        print
        print "3 DALIS. Rezultatai"
        print "   1) ", message
        if ((message != "kelias neegzistuoja.") and (len(path) > 0)):
            print "   2) ",
            printPath(path)
            print

filenames = ["../tests/test1.txt" , "../tests/test2.txt", "../tests/test3.txt", "../tests/test4.txt", "../tests/test5.txt", "../tests/test6.txt"]

for fn in filenames:
    if askForInput(fn):
        data = getData(fn)
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

        doFC(rules, facts, target)



print "done"
