diag = '3,225,1,225,6,6,1100,1,238,225,104,0,1101,37,34,224,101,-71,224,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1002,113,50,224,1001,224,-2550,224,4,224,1002,223,8,223,101,2,224,224,1,223,224,223,1101,13,50,225,102,7,187,224,1001,224,-224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,1101,79,72,225,1101,42,42,225,1102,46,76,224,101,-3496,224,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,1102,51,90,225,1101,11,91,225,1001,118,49,224,1001,224,-140,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,2,191,87,224,1001,224,-1218,224,4,224,1002,223,8,223,101,4,224,224,1,224,223,223,1,217,83,224,1001,224,-124,224,4,224,1002,223,8,223,101,5,224,224,1,223,224,223,1101,32,77,225,1101,29,80,225,101,93,58,224,1001,224,-143,224,4,224,102,8,223,223,1001,224,4,224,1,223,224,223,1101,45,69,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,226,226,224,102,2,223,223,1005,224,329,101,1,223,223,108,677,226,224,102,2,223,223,1005,224,344,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,359,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,374,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,389,101,1,223,223,1108,677,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,108,677,677,224,102,2,223,223,1005,224,419,101,1,223,223,7,226,677,224,1002,223,2,223,1006,224,434,1001,223,1,223,107,226,677,224,102,2,223,223,1005,224,449,101,1,223,223,1108,677,677,224,1002,223,2,223,1006,224,464,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,494,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,509,1001,223,1,223,107,677,677,224,102,2,223,223,1006,224,524,1001,223,1,223,8,226,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1007,677,226,224,102,2,223,223,1006,224,554,1001,223,1,223,1007,226,226,224,1002,223,2,223,1005,224,569,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,584,101,1,223,223,108,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,614,1001,223,1,223,1107,226,677,224,102,2,223,223,1006,224,629,1001,223,1,223,1008,226,677,224,102,2,223,223,1005,224,644,101,1,223,223,1107,226,226,224,102,2,223,223,1006,224,659,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226'
# diag = '3,225,1,225,6,6,1100,1,238,225'
# diag = '1002,4,3,4,33'
# diag = '3,9,8,9,10,9,4,9,99,-1,8'
# diag = '3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9'
# diag = '3,3,1105,-1,9,1101,0,0,12,4,12,99,1'
# diag = '3,3,1108,-1,8,3,4,3,99'
# diag = '3,3,1107,-1,8,3,4,3,99'
diag = '3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99'
# ZAPEO SAM OVDJE. IZ NEKOG RAZLOGA NE DOBIJAM 999

def getDiagnosticCode():
    # return getParameterModeInstruction('1002')
    inp = '7'
    outp = None
    diagList = diag.split(',')
    i = 0
    while True:
    # for i in range(len(diagList)):
        param = diagList[i]
        instruction = getParameterModeInstruction(param)
        # print('Param {} - Immediate mode: {}'.format(param, isImmediateMode(param)))
        if param == '99':
            break
        elif instruction[0] == '1':
            position1 = int(diagList[i+1]) if instruction[1] == '0' else i + 1
            position2 = int(diagList[i+2]) if instruction[2] == '0' else i + 2
            position3 = int(diagList[i+3]) if instruction[3] == '0' else i + 3
            diagList[position3] = str(int(diagList[position1]) + int(diagList[position2]))
            i += 4
        elif instruction[0] == '2':
            position1 = int(diagList[i+1]) if instruction[1] == '0' else i + 1
            position2 = int(diagList[i+2]) if instruction[2] == '0' else i + 2
            position3 = int(diagList[i+3]) if instruction[3] == '0' else i + 3
            diagList[position3] = str(int(diagList[position1]) * int(diagList[position2]))
            i += 4
        elif instruction[0] == '3':
            if instruction[1] == '0':
                position = int(diagList[i+1])
                diagList[position] = inp
            elif instruction[1] == '1':
                diagList[i+1] = inp
            i += 2
        elif instruction[0] == '4':
            if instruction[1] == '0':
                position = int(diagList[i+1])
                outp = diagList[position]
            elif instruction[1] == '1':
                outp = diagList[i+1]
            i += 2
            print(outp)
        elif instruction[0] == '5':
            if instruction[1] == '0' and int(diagList[int(diagList[i+1])]) != 0:
                i = int(diagList[int(diagList[i+2])])
            elif instruction[1] == '1' and int(diagList[i+1]) != 0:
                i = int(diagList[i+2])
            else:
                i += 3
        elif instruction[0] == '6':
            if instruction[1] == '0' and int(diagList[int(diagList[i+1])]) == 0:
                i = int(diagList[int(diagList[i+2])])
            elif instruction[1] == '1' and int(diagList[i+1]) == 0:
                i = int(diagList[i+2])
            else:
                i += 3
        elif instruction[0] == '7':
            val1 = diagList[i+1] if instruction[1] == '1' else diagList[int(diagList[i+1])]
            val2 = diagList[i+2] if instruction[1] == '1' else diagList[int(diagList[i+2])]
            val3 = '1' if int(val1) < int(val2) else '0'
            if instruction[3] == '0':
                diagList[int(diagList[i+3])] = val3
            elif instruction[3] == '1':
                diagList[i+3] = val3
            i += 4
        elif instruction[0] == '8':
            val1 = diagList[i+1] if instruction[1] == '1' else diagList[int(diagList[i+1])]
            val2 = diagList[i+2] if instruction[1] == '1' else diagList[int(diagList[i+2])]
            val3 = '1' if val1 == val2 else '0'
            if instruction[3] == '0':
                diagList[int(diagList[i+3])] = val3
            elif instruction[3] == '1':
                diagList[i+3] = val3
            i += 4

        # else:
        #     instruction2 = getParameterModeInstruction(param)
        #     i = processInstruction(instruction2, diagList, i, param)


    return outp

def getParameterModeInstruction(param):
    ret = []
    optcode = param[-1]
    ret.append(optcode)
    if len(param) >= 3:
        ret.append(param[-3])
    else:
        ret.append('0')

    if len(param) >= 4:
        ret.append(param[-4])
    else:
        ret.append('0')

    if len(param) >= 5:
        ret.append(param[-5])
    else:
        ret.append('0')

    # ret.append(optcode)
    # j = -3
    # k = 1
    # while True:
    #     if len(param) >= abs(j):
    #         mode = param[j]
    #         ret.append(mode)
    #         j -= 1
    #         k += 1
    #     else:
    #         break
    return ret

def processInstruction(instruction, diagList, position, param):
    operation = instruction[0]
    # for i in range(1, len(instruction)):
    mode1 = instruction[1]
    value1 = ''
    if mode1 == '0': # position mode
        value1 = diagList[int(diagList[position + 1])]
    elif mode1 == '1': # immediate mode
        value1 = diagList[position + 1]

    mode2 = instruction[2]
    value2 = ''
    if mode2 == '0': # position mode
        value2 = diagList[int(diagList[position + 2])]
    elif mode2 == '1': # immediate mode
        value2 = diagList[position + 2]

    operationResult = 0
    if operation == '1':
        operationResult = int(value1) + int(value2)
    elif operation == '2':
        operationResult = int(value1) * int(value2)
    
    mode3 = '0'
    if len(instruction) > 3:
        mode3 = instruction[2]
    if mode3 == '0': # position mode
        diagList[int(diagList[position + 3])] = str(operationResult)
    elif mode3 == '1': # immediate mode
        diagList[position + 2] = str(operationResult)

    return position + 4