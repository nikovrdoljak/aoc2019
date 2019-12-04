p1 = 234208
p2 = 765869

def howManyValidPasswords():
    s = 0
    for p in range(234208, 765869 + 1):
        if isValidPassword(p):
            s += 1
    return s

def howManyValidPasswords2():
    s = 0
    for p in range(234208, 765869 + 1):
        if isValidPassword2(p):
            s += 1
    return s

def isValidPassword2(pwd):
    spwd = str(pwd)
    isSixDigit = False
    hasTwoAdjacentDigits = False
    hasExactlyTwoAdjacentDigits = False
    digitsNeverDecrease = True
    twoDigitsMatch = False
    countAdjacentDigits = 0
    countDoubles = 0

    if ( pwd >= 100000 and pwd <= 999999 ):
        isSixDigit = True

    cPrev = ''
    group = ''
    groups = []
    nPrev = 0
    for c in spwd:

        if c == cPrev:
            group += c
        elif c != cPrev and len(group) > 0:
            groups.append(group)
            group = c
        else: 
            group = c

        n = int(c)
        if n < nPrev:
            digitsNeverDecrease = False
        nPrev = n
        cPrev = c

    groups.append(group)

    for g in groups:
        if len(g) == 2:
            hasExactlyTwoAdjacentDigits = True

    return isSixDigit and hasExactlyTwoAdjacentDigits and digitsNeverDecrease

def isValidPassword(pwd):
    spwd = str(pwd)
    isSixDigit = False
    hasTwoAdjacentDigits = False
    digitsNeverDecrease = True

    if ( pwd >= 100000 and pwd <= 999999 ):
        isSixDigit = True

    cPrev = ''
    nPrev = 0
    for c in spwd:
        if c == cPrev:
            hasTwoAdjacentDigits = True
        n = int(c)
        if n < nPrev:
            digitsNeverDecrease = False
        nPrev = n
        cPrev = c

    return isSixDigit and hasTwoAdjacentDigits and digitsNeverDecrease