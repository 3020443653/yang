import yaml
import pytest
def add_fuction(a,b):
    return a+b
#演示参数数据从文件读取
'''
@pytest.mark.parametrize("a,b ,expected",
                        yaml.safe_load(open("./data.yml"))["data"],
                        ids=yaml.safe_load(open("./data.yml"))["myid"] )
'''
#读文件步骤可以抽离出来，为单独的函数
def get_data():
    with open("./data.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        add_datas = datas["data"]
        add_ids = datas["myid"]
        return [add_datas,add_ids]
@pytest.mark.parametrize(" a,b,expected",
                         get_data()[0],
                         ids=get_data()[1])
def test_add(a,b,expected):
    assert  add_fuction(a,b) == expected