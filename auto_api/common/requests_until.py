# -*- coding: utf-8 -*-
# @Author: hhqdsj
import requests


class RequestsUntil:


    # 请求方式
    @classmethod
    def requests_method(cls, url,method=None, **kwargs):
        if method:
            if method.lower() == "post":
                # post请求
                return requests.post(url=url, **kwargs)
            else:
                # get请求
                return requests.get(url=url,**kwargs)
        else:
            return requests.get(url=url, **kwargs)


