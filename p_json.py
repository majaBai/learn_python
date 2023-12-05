import json

def dic_to_json(data):
    print(json.dumps(data))

def json_to_dic(str):
    return json.loads(str)

def main():
    # 三引号允许一个字符串跨多行
    data = '''{"key1" : "value1", "key2" : "value2"}'''
    # dic_to_json(data)

    dic = json_to_dic(data)
    print(dic['key2'])

main()