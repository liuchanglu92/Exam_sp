from configs.config import HOST
import requests
import hashlib
def get_md5(pwd):
    md5 = hashlib.md5()
    md5.update(pwd.encode("utf-8"))
    return  md5.hexdigest()
class Login:
    def login(self,indata,mode=True):
        url =  f'{HOST}/api/loginS'
        payload = indata
        indata["password"] = get_md5(indata["password"])
        resp = requests.post(url,json=indata)
        if mode:
            return resp.json()["token"]
        else:
            return  resp.json()

if __name__ == '__main__':
    res = Login().login({"username":"20154084","password":"123456"})
    print(res)
    print(get_md5("123456"))