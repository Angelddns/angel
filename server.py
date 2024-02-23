# from flask import  jsonify
# from flask import  request
# import json
# from flask import Flask
#
#
#
# app=Flask(__name__)#创建一个Flask应用实例
# def get_word(word): #定义一个函数，接受一个单词作为参数，目前函数体仅返回接收到的单词
#    return int(word)*int(word)
# # def get_resout(num): #定义一个函数，接受一个单词作为参数，目前函数体仅返回接收到的单词
# #    return int(num)*int(num)
#
#
# @app.route("/nlp/words",methods=["GET","POST"])#使用app.route装饰定义路由器，指定url路径和接受的请求方法
# def nlp_service():#定义处理该路由请求的函数
#    data=request.get_data()#从请求中获取数据
#    result_data=json.loads(data)#将获取的数据从json格式解析为python字典
#    word=result_data.get("word","")#从解析后的数据中获取键为“word”的值，如果不存在则默认为空字符串
#    value=get_word(word)#调用get_word函数处理获取到的单词
#    return   jsonify( {"code":200 , "result":value } ) #使用jsonify函数构建JSON格式的响应，包含状态码和处理结果。
#
# if __name__=="__main__": #判断是否为主程序运行，而非模块导入
#    app.run(host='0.0.0.0',port=50001)#启动flask应用，指定监听的主机地址和端口号
#

from flask import jsonify
from flask import request
import json
from flask import Flask

app=Flask(__name__)

def get_word(word):
    return word*word     #{}

@app.route('/nlp/words',methods=['GET','POST'])
def nlp_service():
    data=request.get_data()
    result_data=json.loads(data)
    print(result_data)
    word=result_data.get('word','')
    value=get_word(word)
    return jsonify({'code':200,'result':value})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=50001)