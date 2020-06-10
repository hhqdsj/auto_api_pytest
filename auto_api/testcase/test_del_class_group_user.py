# -*- coding: utf-8 -*-
# @Author: hhqdsj

import json
import pytest
from auto_api.common.requests_until import RequestsUntil



'''
测试数据未参数化的例子
'''


class TestGmsc:

    test_data = ["17644444444", ]

    @pytest.mark.parametrize("get_user_id", test_data, indirect=True)   #数据驱动，用例参数化
    def test_del_class_user(self,get_user_id):

        # 文件路径
        self.file = "class_group_del_uder.yaml"

        self.conf,self.uid,self.environment = get_user_id
        self.datas = self.conf.get_yaml_data(self.file)

        # 读取class_group_del_uder.yaml中的接口数据
        url,headers,data,method = self.conf.read_data(self.datas,"url", "headers", "data","method")

        # 重写url中的环境参数
        url["environment"] = self.environment
        # 拼接接口地址
        url = url["protocol"] + url["environment"] + url["ip"]

        # 将class_group_del_uder.yaml文件中的  MemberToDel_Account  变量重新赋值为get_user_id的返回值uid
        data["MemberToDel_Account"][0]=str(self.uid)
        datas=json.dumps(data)
        # 接口请求
        r=RequestsUntil.requests_method(method=method,url=url, data=datas, headers=headers)
        # 接口的响应数据
        res = r.json()

        # 断言
        assert r.status_code == 200
        assert res["info"] == "成功"








if __name__ == '__main__':
    pytest.main(["-s","test_del_class_group_user.py"])