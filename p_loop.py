def printNum():
    for i in range(1, 11):
        print(i)

def printPattern(n):
    for j in range(1, n + 1):
        r = ''
        for i in range(1, j + 1):
            r += str(i) + ' '
        print(r)

def printPattern3(n = 9):
    middle = n // 2
    p = "* "
    for i in range(1, n + 1):
        if(i <= middle + 1):
            print(p * i)
        else:
            print(p * (middle + 1 - (i - (middle + 1))))

def printPattern2(n):
    for j in range(1, n + 1):
        r = ''
        for i in range(1, n + 2 - j):
            r = str(i) + ' ' + r
        print(r)


def sum(n):
   res = 0
   for i in range(n + 1):
       res += i
   print(res)

def multipOfnum(n):
   for i in range(1, 11):
       print(n * i)

def displayNum(arr):
    for i in arr:
        if i % 5 == 0 and i <= 150:
            print(i)
        if i > 500:
            break

def numCount(n):
    res = 0
    while n > 0:
        res += 1
        n = n // 10
    print(res)

def reverseList(arr):
    arr.reverse()
    for i in arr:
        print(i)

def displayNumBetween(n, m):
    for i in range(n, m + 1):
        print(i)

def showDone(n):
    for i in range(n):
        print(i)
    print('Done!')

def isPrime(n):
    if n < 3:
        return n == 2
    for i in range(2, n):
        if n % i == 0 :
            return False
    return True
    

def primeNumIn(n, m):
    for i in range(n, m):
        if isPrime(i):
            print(i)

def Fibonacci(n):
    first, second = 0, 1
    for i in range(n):
        print(first)
        first, second = second, first + second

def factorialNum(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    print(res)

def reveseInt(n):
    # 反转字符串[::-1]
    print(str(n)[::-1])

def valueAtOdd(arr):
    for i in range(len(arr)):
        if i % 2 != 0:
            print(arr[i])


def cubeOf(n):
    print(n**3)

def sumOfSeries(n):
    sum = 0
    for i in range(1, n + 1):
        cur = 0
        for j in range(0, i):
            cur += 2 * (10 ** j)
        sum += cur
    print(sum)


def main():
    # printNum()

    # printPattern(5)

    # sum(10)

    # multipOfnum(2)

    # displayNum([12, 75, 150, 180, 145, 525, 50])

    # numCount(745)

    # printPattern2(5)

    # reverseList([10, 20, 30, 40, 50])

    # displayNumBetween(-10, -1)

    # showDone(5)

    # primeNumIn(25, 50)

    # Fibonacci(10)

    # factorialNum(5)

    # reveseInt(76542)

    # valueAtOdd([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    # cubeOf(6)

    # sumOfSeries(5)

    printPattern3(11)


main()