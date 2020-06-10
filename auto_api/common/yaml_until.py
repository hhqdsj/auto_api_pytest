# -*- coding: utf-8 -*-
# @Author: hhqdsj

import yaml
import os
from auto_api.conf import setting


class YamlUntil:

    yaml_path=setting.api_path

    # 读取yaml数据
    @classmethod
    def get_yaml_data(cls,yaml_data,yaml_data_path=yaml_path):
        cls.yaml_path = os.path.join(yaml_data_path, yaml_data)
        with open(cls.yaml_path, 'r', encoding="utf-8") as f:
            file_data = f.read()
        cls.data = yaml.load(file_data, Loader=yaml.FullLoader)
        return cls.data

    # 读取接口中的参数,根据传参输出对应内容
    @classmethod
    def read_data(cls, datas, *args):
        cls.parameter = []
        cls.datas=datas
        for args_key in args:
            if args_key == "url":
                cls.url = cls.datas.get("url")
                cls.parameter.append(cls.url)
            elif args_key == "method":
                cls.method = cls.datas.get("method")
                cls.parameter.append(cls.method)
            elif args_key == "headers":
                cls.headers = cls.datas.get("headers")
                cls.parameter.append(cls.headers)
            elif args_key == "params":
                cls.params = cls.datas.get("params")
                cls.parameter.append(cls.params)
            elif args_key == "data":
                cls.data = cls.datas.get("data")
                cls.parameter.append(cls.data)
        return cls.parameter



