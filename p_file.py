import sys
# with open('test.txt', 'r') as f:
#     print(f.read())
    # for line in f.readlines():
    #     print(line.strip())


try:
    # f = open(r'D:\learnPython\learn_python\test.txt', 'r')
    f = open('test.txt', 'r')
    print('f', f)
    print(f.read())
finally:
    print('finally')
    if f:
        f.close()