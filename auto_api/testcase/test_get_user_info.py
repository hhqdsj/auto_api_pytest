# -*- coding: utf-8 -*-
# @Author: hhqdsj

import pytest
from auto_api.conf.config_until import ConfigUntil
from auto_api.common.requests_until import RequestsUntil


'''
测试数据全部参数化例子
'''

class TestSso:

    conf=ConfigUntil()
    # 从D:\requests\auto_api\conf\conf.yaml读取environment的值
    environment=conf.get_environment
    # 测试用例数据
    test_data=conf.test_get_user_info_data
    # 数据库参数
    db_parameters=[]
    db_parameters.append(conf.get_database_conf)



    # 通过手机好获取用户信息
    @pytest.mark.parametrize("account,info,sql",test_data)#用例数据参数化
    @pytest.mark.parametrize("database", db_parameters, indirect=True)#数据库连接参数参数化
    def test_get_user_info(self,database,account,info,sql):

        mysql, conn=database
        db_data = mysql.run_sql(conn, sql)
        file=self.conf.get_user_info_by_phone_api

        #获取D:\requests\auto_api\api\get_user_info_by_phone.yaml文件中的原始接口数据
        datas=self.conf.get_yaml_data(file)
        #获取接口的初始值
        url,headers,params,method=self.conf.read_data(datas,"url","headers","params","method")
        url["environment"] = self.environment
        url=url["protocol"]+url["environment"]+url["ip"]
        params["account"]=account

        # 请求接口
        r=RequestsUntil.requests_method(url=url, params=params, headers=headers)
        #获取响应
        res = r.json()
        uid = res["data"]["UserData"][0]["Uid"]
        assert r.status_code == 200
        assert res["info"] == info
        assert uid == db_data["uid"]





if __name__ == '__main__':
    pytest.main(["-s","test_get_user_info.py"])
