# -*- coding: utf-8 -*-
# @Author: hhqdsj
from auto_api.common.yaml_until import YamlUntil
from auto_api.conf import setting



class ConfigUntil(YamlUntil):
    conf_data_path = setting.conf_data_path
    case_data_path = setting.case_data_path
    api_path = setting.api_path
    def __init__(self):
        self.file_path = self.get_yaml_data("conf.yaml", yaml_data_path=self.conf_data_path)


    """
    测试环境
    """
    @property
    def get_environment(self):
        return self.file_path["environment"]




    """
    数据库配置
    """
    @property
    def get_database_conf(self):
        return self.file_path["database_conf"]


    """
    API文件路径
    """
    @property
    # 返回get_user_info_by_phone.yaml的文件名
    def get_user_info_by_phone_api(self):
        return self.file_path["get_user_info_by_phone_api"]


    """
    测试用例文件路径
    """
    @property
    #返回test_get_user_info1.py中所需要的用例数据
    def test_get_user_info_data(self):
        return self.get_yaml_data(self.file_path.get("test_get_user_info_case"),self.case_data_path)




