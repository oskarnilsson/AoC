

def run_program(code, noun, verb):
    # Initial values
    code[1] = noun
    code[2] = verb
    i = 0
    for i in range(0, len(code), 4):
        opcode = code[i]
        if opcode == 99:
            break

        index1 = code[i + 1]
        index2 = code[i + 2]
        indexDest = code[i + 3]
        val1 = code[index1]
        val2 = code[index2]
        if opcode == 1:
            # Addition
            code[indexDest] = val1 + val2
        elif opcode == 2:
            # Multiplication
            code[indexDest] = val1 * val2

    return code[0]

if __name__ == '__main__':
    # Part 1, noun = 12, verb = 2
    f = open("2_intCode.txt", "r")
    stringCode = list(f.readline().split(","))
    intCode = list(map(int, stringCode))

    runCode = intCode.copy()
    print(run_program(runCode,12,2))
    #19690720
    for n in range(1,100):
        for v in range (1,100):
            runCode = intCode.copy()
            result = run_program(runCode, n, v)
            if(result == 19690720):
                print(n)
                print(v)
                print(100*n + v)