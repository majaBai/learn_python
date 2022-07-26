def productOftwoNum(n, m):
    if m * n <= 1000:
        print(m * n)
    else:
        print(m + n)

def sumRange(n):
    for i in range(n):
        if i >= 1:
            print(i + i -1)
        else:
            print(i)

def charAtEvenIndex(str):
    print([str[i] for i in range(len(str)) if i % 2 == 0])


def remove_chars(str, num):
    print(str[num:])

def firstSameAsLast(arr):
    print(arr[0] == arr[-1])

def devidedBy5(arr):
    print([i for i in arr if i % 5 == 0])

def countOfSubstring(str, substr):
    r = str.count(substr)
    print(f'{substr} appeared {r} times')

def repeatPrint(n):
    print((str(n) + ' ') * n, end='')

def isPalindrome(num):
    strnum = str(num)
    length = len(strnum)
    middle = length // 2
    for i in range(middle):
        if strnum[i] != strnum[- 1 - i]:
            print(False)
            return
    print(True)

def oddEvenMerge(arr1, arr2):
    r1 = [i for i in arr1 if i % 2 != 0]
    r2 = [i for i in arr2 if i % 2 == 0]
    print(r1 + r2)

def reverseDigit(n):
    strnum = str(n)
    for i in range(len(strnum)):
        print(strnum[-1 - i] + ' ', end=" ")

def caculateTax(n):
    t = "Total tax to pay is"
    if n < 10000:
        print(t, 0)
    elif n <= 20000:
        print(t, (n-10000) * 0.1)
    else:
        print(t, 10000 * 0.1 + (n-20000) * 0.2)

def multiplicationTable():
    i = 1
    while i < 11:
        r = ''
        j = 1
        while j < 11:
            r += str(i * j) + ' '
            j += 1
        print(r)
        i += 1

def halfPyramid(n):
    while n > 0:
        print(('*' + ' ') * n)
        n -= 1

def exponent(base, exp):
    print(base ** exp)

def main ():
    # productOftwoNum(20, 30)

    # sumRange(10)

    # charAtEvenIndex('pynative')

    # remove_chars('pynative', 4)

    # devidedBy5([10, 20, 33, 46, 55])

    # countOfSubstring('Emma is good developer. Emma is a writer', 'Emma')

    # repeatPrint(5)

    # isPalindrome(545)

    # oddEvenMerge([10, 20, 25, 30, 35], [40, 45, 60, 75, 90])

    # reverseDigit(45679)

    # caculateTax(45000)

    # multiplicationTable()

    # halfPyramid(5)

    exponent(2, 5)



main()