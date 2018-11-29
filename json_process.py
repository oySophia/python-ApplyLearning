#coding=utf-8
#/usr/bin/python

import json

def json_process(dic1, dic2):
    print "now in the json_process"
    #encoding: put python content into json--------dump(文件流) & dumps(字符串)
    print type(dic1)
    python_to_json = json.dumps(dic1, ensure_ascii=False)
    print python_to_json
    print type(python_to_json)

    #decoding: put json content into python ------load & loads
    json_to_python = json.loads(python_to_json)
    print json_to_python
    print type(json_to_python)

    print "+++++++++++now in the dic field testing"
    print type(dic2)
    python_to_json = json.dumps(dic2, ensure_ascii=False)
    print type(python_to_json)
    print python_to_json
    json_to_python = json.loads(python_to_json)
    print type(json_to_python)
    print json_to_python
    print json_to_python['username']
    tmp = json_to_python['username']
    json_to_python['username'] = tmp
    print json_to_python


if __name__ == "__main__":
    dic1 = [{"username":"测试","age":16},(2,3),1]
    dic2 = {'type': 'dic1', 'username': '测试', 'age': 16}
    json_process(dic1, dic2)
    #json_process(dic2)
    print "now in the main func"