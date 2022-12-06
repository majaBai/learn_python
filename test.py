def change(a):
    print('2', id(a))   # 指向的是同一个对象
    a=10
    print('3', id(a))   # 一个新对象
 
a=1
print('1', id(a))
change(a)
print('4', id(a), a)