# -*- coding: utf-8 -*-
# @Author: hhqdsj

import pytest
from auto_api.conf.config_until import ConfigUntil
from auto_api.common.db import DB
from auto_api.common.requests_until import RequestsUntil


'''
这是一个公共的模块，所有可以复用的方法均可以写入此文件
'''


# 将获取用户ID作为一个功能的方法
@pytest.fixture()
def get_user_id(request):
    '''
    requestde 用法参考：https://www.cnblogs.com/yoyoketang/p/9492132.html
    '''
    # 实例化一个读取配置文件的对象
    conf = ConfigUntil()
    environment = conf.get_environment
    #接口参数文件
    file = conf.get_user_info_by_phone_api
    # 获取接口数据
    datas = conf.get_yaml_data(file)
    # 获取调用者参数化的值
    account=request.param
    # 给接口account参数赋值
    params={
        "account": account
    }

    # 获取接口的初始值
    url, headers, method = conf.read_data(datas, "url", "headers", "method")

    # 重写url中的环境参数
    url["environment"] = environment
    # 拼接接口地址
    url = url["protocol"] + url["environment"] + url["ip"]

    # 请求接口
    r = RequestsUntil.requests_method(url=url, params=params, headers=headers)
    # 获取返回结果
    res = r.json()
    uid = res["data"]["UserData"][0]["Uid"]
    yield conf,uid,environment




# 数据库连接
@pytest.fixture(scope="module")
def database(request):

    host = request.param["host"]
    port =request.param["port"]
    user =request.param["user"]
    passw =request.param["passw"]
    database =request.param["database"]
    charset = request.param["charset"]
    # 链接数据库
    mysql = DB(host, port, user, passw, database, charset)
    conn = mysql.connect()
    yield mysql,conn
    mysql.close_connect(conn)




