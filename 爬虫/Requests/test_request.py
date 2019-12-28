import requests
import json

url = 'http://www.cntour.cn/'#使用get方式抓取数据

strhtml = requests.get(url)
print(strhtml.text)

'''
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'#使用post方式抓取数据

From_data = {'i':'我爱中国',\
    'from':'AUTO',\
        'to':'AUTO',\
    'smartresult':'dict',\
    'client': 'fanyideskweb',\
    'salt':	'15667196591573',\
    'sign':	'f4dcd78f8c2cb9bc761e51c24ce29ac8',\
    'ts': '1566719659157',\
    'bv': 'abf85f8020851128b561472c8a7b924d',\
    'doctype': 'json',\
    'version': '2.1',\
    'keyfrom': 'fanyi.web',\
    'action': 'FY_BY_REALTlME',\
    'typoResult': 'false'}

response = requests.post(url, data=From_data)
content = json.loads(response.text)
print(content)
'''