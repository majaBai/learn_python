
def listIntoDic(l1, l2):
    # d = {}
    # for i in range(len(l1)):
    #     d[l1[i]] = l2[i]
    # print(d)

    print(dict(zip(l1, l2)))

def mergeTwoDic(d1 , d2):
    d3 = d1.copy()
    d3.update(d2)
    print(d3)

def getValueOf(key, d):
    for k in d.keys():
        if(k == key):
            print(d[k])
            return
        elif (type(d[k]) == type({})):
            getValueOf(key, d[k])

def initDictWithDefaut(keys, defVal):
    print(dict.fromkeys(keys, defVal))

def findKeys(keys, d):
    # r = {}
    # for k in keys:
    #         r[k] = d.get(k)
    # print(r)

    r = {k: d[k] for k in keys}
    print(r)


def removeKeys(keys, d):
    # solution1:
    # for k in keys:
    #    del d[k]
    # print(d)

    # solution2:
    # for k in keys:
    #     d.pop(k)
    # print(d)

    # solution3:
    r = {k : d[k] for k in d.keys() - keys}
    print(r)

def checkValue(v, d):
    print(v in d.values())

def renameKey(oldk, newk, d):
    # pop 返回被删除的key所对应的val
    d[newk] = d.pop(oldk)
    print(d)
    
    
def main():
    # listIntoDic(['Ten', 'Twenty', 'Thirty'], [10, 20, 30])

    # mergeTwoDic({'Ten': 10, 'Twenty': 20, 'Thirty': 30}, {'Thirty': 30, 'Fourty': 40, 'Fifty': 50})

    # print(type({'a' : 1}) == type({})) True
    # sampleDict = {
    #     "class": {
    #         "student": {
    #             "name": "Mike",
    #             "marks": {
    #                 "physics": 70,
    #                 "history": 80
    #             }
    #         }
    #     }
    # }
    # getValueOf('history', sampleDict)

    # initDictWithDefaut(['Kelly', 'Emma'], {"designation": 'Developer', "salary": 8000})

    sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
    }
    # findKeys(["name", "salary"], sample_dict)

    # removeKeys(["name", "salary"], sample_dict)

    # checkValue(8000, sample_dict)

    renameKey('city', 'location', sample_dict)


main()