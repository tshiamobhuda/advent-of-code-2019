from common import computeNounVerb
from os import getcwd

f = open(getcwd() + '/data/day2.txt')
intCode = f.readline()
f.close()

solution = computeNounVerb(intCode.split(','))

print(solution)