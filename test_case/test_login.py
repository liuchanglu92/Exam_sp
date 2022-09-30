from tools.yamlControl import get_yaml_data
from libs.login import Login

def test_login_success():
    res = get_yaml_data('../data/logincase.yaml')[1]
    respData = Login().login(res['data'],False)
    print(respData)
    if respData['message'] == res['resp']['message']:
        print("----用例成功-----")
    else:
        print("----用例失败-----")