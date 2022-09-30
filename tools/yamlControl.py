import yaml
def get_yaml_data(fileDir):
    fo = open(fileDir,"r",encoding="utf-8")
    res = yaml.load(fo,Loader=yaml.FullLoader)
    fo.close()
    info = res[0]
    print(info)
    return res

if __name__ == '__main__':
    res = get_yaml_data('../data/logincase.yaml')
    print(res)