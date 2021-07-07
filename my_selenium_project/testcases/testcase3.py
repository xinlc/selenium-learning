"""
基于第三方AI API 实现验证码识别
"""
# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
from lib.ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/184-4", "272526", "a924d4e982ae404b8a068b4d1c7784f2")
r.addFilePara("image", "test.png")
r.addBodyPara("typeId", "34")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
res = r.post()
result = res.text
print(result)
body = res.json()['showapi_res_body']
print(body['Result'])
# print(res.text) # 返回信息
