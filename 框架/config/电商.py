import requests
class 电商():
    def 登录(self,a,b):
            url = "http://www.zhaoapi.cn/user/login"
            querystring = {"mobile":"{}".format(a),"password":"{}".format(b)}
            headers = {
                'Content-Type': "application/x-www-form-urlencoded",
                'cache-control': "no-cache",
                'Postman-Token': "ea94b1f0-b38e-40ab-9bee-6c9f1cd4b4ba"
                }
            response = requests.request("POST", url, headers=headers, params=querystring)
            c = response.json()
            return c
    def 注册(self,a,b):
        url = "http://www.zhaoapi.cn/user/reg"
        querystring = {"mobile": "{}".format(a), "password": "{}".format(b)}
        headers = {
            'Content-Type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
            'Postman-Token': "137ead58-02f7-4db2-8821-b7ce420ee4fe"
        }
        response = requests.request("POST", url, headers=headers, params=querystring)
        x=response.json()
        return x
