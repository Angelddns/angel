import requests
import json

def get_result():
    url="http://127.0.0.1:50001/nlp/words"

    data={"word":5}
    data_json=json.dumps(data)#将字典转为JSON格式的字符串，因为request库在发送请求时，需要字符串格式的数据
    response=requests.post(url,data=data_json)#发送post请求
    print(response.json())#打印相印内容，使用 直接获取json格式的响应数据。

if __name__=="__main__":
    get_result()




