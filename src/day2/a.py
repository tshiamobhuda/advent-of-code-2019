import common
from os import getcwd

f = open(getcwd() + '/data/day2.txt')
strIntCodeProgram = f.readline()
f.close()

solutionIntCodeProgram = common.computeIntCode(strIntCodeProgram.split(','))

print(solutionIntCodeProgram[0])