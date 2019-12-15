
def _opcodeAction(opcode, a, b):
    if opcode == 1:
        return a + b

    if opcode == 2:
        return a * b

def computeIntCode(instructions):
    pos = 0
    while True:
        opcode = int(instructions[pos])

        if opcode == 99:
            break

        aPos = int(instructions[pos+1])
        bPos = int(instructions[pos+2])
        cPos = int(instructions[pos+3])
        aVal = int(instructions[aPos])
        bVal = int(instructions[bPos])
        
        instructions[cPos] = _opcodeAction(opcode, aVal, bVal)
        
        pos += 4

    return instructions

def computeNounVerb(instructions):
    for noun in range(0, 99):
        for verb in range(0, 99):
            instructions[1] = noun
            instructions[2] = verb

            res = computeIntCode(instructions.copy())

            if res[0] == 19690720:
                return 100 * noun + verb