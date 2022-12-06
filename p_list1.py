
def reverseList(l):
    l.reverse()
    print(l)

def concatList(l1, l2):
    # r = []
    # for i in range(len(l1)):
    #     r.append(l1[i] + l2[i])
    # print(r)


    # zip() : This function takes two or more iterables (like list, dict, string), 
    # aggregates them in a tuple, and returns it.
    # r = [i for i in zip(l1, l2)]
    # r = [('M', 'y'), ('na', 'me'), ('i', 's'), ('Ke', 'lly')]
    # print(r)
    print([i + j for i, j in zip(l1, l2)])

def caculateSqure(l):
    print([v * v for v in l])

def concatList2(l1, l2):
    # r = []
    # for i in l1:
    #     for j in l2:
    #         r.append(i + j)
    # print(r)

    print([i + j for i in l1 for j in l2])

def iterate2List(l1, l2):
    # l2.reverse()
    # for j, k in [i for i in zip(l1, l2)]:
    #     print(f'{j} {k}')

    for i, j in zip(l1, l2[::-1]):
        print(i, j)

def removeEmpty(l):
    print(list(filter(None, l)))

def replaceFirstItem(l, t):
    i = l.index(t)
    l[i] = 200
    print(l)

def removeAllItem(l, t):
   print([i for i in l if i != t])

def main():
    # reverseList([100, 200, 300, 400, 500])

    # concatList(["M", "na", "i", "Ke"], ["y", "me", "s", "lly"])

    # caculateSqure([1, 2, 3, 4, 5, 6, 7])

    # concatList2(["Hello ", "take "], ["Dear", "Sir"])

    # iterate2List([10, 20, 30, 40], [100, 200, 300, 400])

    # removeEmpty(["Mike", "", "Emma", "Kelly", "", "Brad"])\

    # replaceFirstItem([5, 10, 15, 20, 25, 50, 20], 20)

    removeAllItem([5, 10, 15, 20, 25, 50, 20], 20)



main()