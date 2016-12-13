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
