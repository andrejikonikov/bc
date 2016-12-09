# Author: Andrej Ikonikov andrejikonikov@gmail.com
# this code was developed to be used as input handler
# it accepts filename of file with rules and returns
# an array of rules.

def getData(filename):
    state = "random"
    rules = []
    facts = []
    target = []

    f = open(filename, 'r')

    for line in f:

        if ((line[0] == '1') and (line[1] == ')')):
            state = "rules"
        elif ((line[0] == '2') and (line[1] == ')')):
            state = "facts"
        elif ((line[0] == '3') and (line[1] == ')')):
            state = "target"

        elif state == "rules":
            # print "rule:", line
            line = line.strip()
            rules.append(line)
        elif state == "facts":
            # print "fact:", line
            line = line.strip()
            facts.append(line)
        elif state == "target":
            # print "target:", line
            line = line.strip()
            target.append(line)

    return rules, facts, target
