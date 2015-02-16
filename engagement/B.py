__author__ = 'julenka'

lineA="qwbsgftspihhejwotrcvdzknsoc"
lineB="earoclexwolgdrbyalnelieukwe"
lineAB = zip(lineA, lineB)

aToB = {x:y for x,y in lineAB}
bToA = {y:x for x,y in lineAB}

one =   "warofthering"
two =   "twilightstruggle"
three = "battlestargalactica"
four =  "settlersofcatan"
five =  "hanabi"
six =   "dominion"

one_instructions = "you roll some dice i roll some dice you set one die aside and move some pieces of plastic a few inches"

all_lst = [one,two,three,four,five,six]

def translate(mp, s):
    return "".join([mp[x] if x in mp else x for x in s])

def translate2(ab, s):


def toAlpha(n):
    return chr(97 + n - 1)

def remove(strA, strB):
    '''
    :param strA:
    :param strB:
    :return: strA - strB
    '''
    a = list(strA)
    for c in strB:
        if c in a:
            a.remove(c)
    return "".join(a)

