
def reverseTulpe(t):
    print(t[::-1])

def unpackTuple(t):
    a, b, c, d = t
    print(a)
    print(b)
    print(c)
    print(d)

def swapTuples(t1, t2):
    t1, t2 = t2, t1
    print(t1)
    print(t2)

def copyItem(t):
    print(tuple(i for i in t if i == 44 or i == 55))

def modifyTuple(t):
    t[1][0] = 222
    print(t)

def sortTuple(t):
   print(tuple(sorted(t, key = lambda x : (x[1]))))

def occurenceCount(t, g):
    # print(list(t).count(g))
    print(t.count(g))

def checkSame(t):
    print(all(i == t[0] for i in t))

def main():
    # reverseTulpe((10, 20, 30, 40, 50))

    # unpackTuple((10, 20, 30, 40))

    # swapTuples((11, 22), (99, 88))

    # copyItem((11, 22, 33, 44, 55, 66))

    # modifyTuple((11, [22, 33], 44, 55))

    # sortTuple((('a', 23),('b', 37),('c', 11), ('d',29)))

    # occurenceCount((50, 10, 60, 70, 50), 50)

    checkSame((45, 45, 45, 43))


main()