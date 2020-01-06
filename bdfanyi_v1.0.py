import http.client
import hashlib
import json
import urllib
import random
 
def baidu_translate(content):
    appid = '20191218000367407' #这个appid 请访问 http://api.fanyi.baidu.com/ 注册认证后获得
    secretKey = 'MnFJgUOPIJmlncyEcgWK' #这个秘钥 请访问 http://api.fanyi.baidu.com/ 注册认证后控制台查看
    httpClient = None
    myurl = '/api/trans/vip/translate'  #百度翻译接口
    q = content
    fromLang = 'auto' # 源语言
    toLang = 'zh'   # 翻译后的语言
    print('默认是翻译为中文，不输入请按回车')
    inlag = input('请输入转换的语言：')
    if inlag == "英语":
        toLang = 'en'
    elif inlag == "法语":
        toLang = "fra"
    elif inlag == "韩语":
        toLang = "kor"
    elif inlag == "西班牙语":
        toLang = "de"
    elif inlag == "荷兰语":
        toLang = "nl"
    elif inlag == "日语":
        toLang = "jp"
    else:
        toLang = "zh"
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign
 
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        jsonResponse = response.read().decode("utf-8")# 获得返回的结果，结果为json格式
        js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
        dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
        print(dst) # 打印结果
        print('*****************************************')
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
 
if __name__ == '__main__':
    while True:
        print("请输入要翻译的内容,如果退出输入q")
        content = input()
        if (content == 'q'):
            break
        baidu_translate(content)
