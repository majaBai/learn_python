
from ctypes import Union


def addList(s, l):
    s.update(l)
    print(s)

def intersectionOf(s1, s2):
    print(s1.intersection(s2))

def unionOf(s1, s2):
    print(s1.union(s2))

def removeSame(s1, s2):
    s1.difference_update(s2)
    print(s1)

def filterAs(s1, s2):
    # u = s1.union(s2)
    # d = s1.intersection(s2)
    # u.difference_update(d)
    s1.symmetric_difference_update(s2)
    print(s1)

def hasCommon(s1, s2):
    if s1.intersection(s2):
        print(s1.intersection(s2))

def remove2(s1, s2):
    s1.intersection_update(s2)
    print(s1)
#    print(s1 & s2)



def main():
    # addList({"Yellow", "Orange", "Black"}, ["Blue", "Green", "Red"])

    # intersectionOf({10, 20, 30, 40, 50}, {30, 40, 50, 60, 70})

    # unionOf({10, 20, 30, 40, 50}, {30, 40, 50, 60, 70})

    # removeSame({10, 20, 30}, {20, 40, 50})

    # filterAs({10, 20, 30, 40, 50}, {30, 40, 50, 60, 70})

    # hasCommon({10, 20, 30, 40, 50}, {60, 70, 80, 90, 10})

    remove2({10, 20, 30, 40, 50, 80}, {30, 40, 50, 60, 70})


main()