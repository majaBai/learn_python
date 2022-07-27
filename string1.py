
import string

def createStr(s):
    print(s[0]+s[len(s)//2]+s[-1])

def middleThreeChar(s):
    m = len(s) // 2
    print(s[m - 1] + s[m] + s[m + 1])

def dividby75():
    # _2_2_2 任意填写3个数字，找出能被 72 整除的所有数
    b1 = 2 * 10000
    b2 = 2 * 100
    b3 = 2
    count = 0
    for i in range(1, 10):
        first = i * 100000
        for j in range(10):
            middle = j * 1000
            for k in range(10):
                last = k * 10
                num = first + b1 + middle + b2 + last + b3
                if num % 72 == 0:
                    print(num)
                    count += 1
    print(f'total:{count}')

def appendMiddle(s1, s2):
    m = len(s1) // 2
    print(s1[0:m] + s2 + s1[m:])

def merge3Part(s1, s2):
    m1 = len(s1) // 2
    m2 = len(s2) // 2
    print(f'{s1[0]}{s2[0]}{s1[m1]}{s2[m2]}{s1[-1]}{s2[-1]}')

def sortString(s):
    lower = ''
    upper = ''
    for char in s:
        if char.islower():
            lower += char
        else:
            upper += char
    print(lower + upper)

def typeCount(s):
    chars_c = 0
    digits_c = 0
    symbol_c = 0
    for c in s:
        if c.isalpha():
            chars_c += 1
        elif c.isdigit():
            digits_c += 1
        else:
            symbol_c += 1
    print(f'Chars = {chars_c}')
    print(f'Digits = {digits_c}')
    print(f'Symbol = {symbol_c}')

def concatHeadAndTail(s1 , s2):
    if len(s1) > len(s2):
        return concatHeadAndTail(s2, s1)
    r = ''
    length1 = len(s1)
    length2 = len(s2)
    for i in range(length1):
        r += (s1[i] + s2[-i - 1])
    # if length1 != length2:
    #     r += s2[0 : (length2 - length1)]
    print(r)
    return r

def checkBalance(s1, s2):
    r = True
    for c1 in s1:
        if c1 not in s2:
            r = False
            break
    print(r)

def substringCount(s, sub):
    print(s.lower().count(sub.lower()))

def caculateSumAndAverage(s):
    count = 0
    sum = 0
    for c in s:
        if c.isdigit():
            count += 1
            sum += int(c)
    print(f'Sum is: {sum} Average is {sum / count}')

def countOfAllChar(s):
    dict = {}
    for c in s:
        # if c in dict:
        #     dict[c] += 1
        # else:
        #     dict[c] = 1

        # count = s.count(c)
        # dict[c] = count

        dict[c] = dict.get(c, 0) + 1

    print(str(dict))

def reverseStr(s):
    # print(''.join(list(reversed(s))))
    print(s[::-1])

def lastPosition(s, sub):
    print(s.rfind(sub))

def splitOnhyphens(s):
    for c in s.split('-'): print(c)

def removeEmpty(l):
    print([s for s in l if s])
    # print(list((s for s in l if s)))

def removeSymbol(s):
    # r = []
    # for c in s:
    #     if c.isalnum() or c.isspace():
    #         r += c
    # print(r)
    print(''.join(c for c in s if c.isalnum() or c.isspace()))

def keepDigit(s):
    print(''.join(c for c in s if c.isdigit()))

def keepAlphAndNum(s):
    t = s.split(' ')
    for c in t:
        if c.isalnum() and (not c.isalpha()) and (not c.isdigit()):
            print(c)

def replaceSymbol(s):
    # r = ''
    # for c in s:
    #     if c.isalnum() or c.isspace():
    #         r += c
    #     else:
    #         r += "#"
    # print(r)

    t = "#"
    for m in string.punctuation:
        s = s.replace(m, t)
    print(s)

def main():
    # createStr('James')

    # middleThreeChar('JhonDipPeta')

    # dividby75()

    # appendMiddle("Ault", "Kelly")

    # merge3Part("America", "Japan")

    # sortString('PyNaTive')

    # typeCount('P@#yn26at^&i5ve')

    # concatHeadAndTail("Abc", "Xyz")

    # checkBalance("Ynf", "PYnative")

    # substringCount("Welcome to USA. usa awesome, isn't it?", 'usa')

    # caculateSumAndAverage("PYnative29@#8496")

    # countOfAllChar("Apple")

    # reverseStr("PYnative")

    # lastPosition("Emma is a data scientist who knows Python. Emma works at google.", 'Emma')

    # splitOnhyphens('Emma-is-a-data-scientist')

    # removeEmpty(["Emma", "Jon", "", "Kelly", "None", "Eric", ""])

    # removeSymbol("/*Jon is @developer & musician")

    # keepDigit('I am 25 years and 10 months old')

    # keepAlphAndNum("Emma25 is Data scientist50 and AI Expert")

    replaceSymbol('/*Jon is @developer & musician!!')


main()