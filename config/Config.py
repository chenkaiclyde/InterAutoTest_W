import os

# 1.获取当前项目基本路径
# 获取当前项目的绝对路径
from utils.YamlUtil import YamlReader

current = os.path.abspath(__file__)
# print(current)  # C:\Users\Clyde\Desktop\InterAutoTest_W\config\Config.py
BASE_DIR = os.path.dirname(os.path.dirname(current))
# print(BASE_DIR)  # C:\Users\Clyde\Desktop\InterAutoTest_W

# 定义config目录的路径
_config_path = BASE_DIR + os.sep + "config"
# print(_config_path)  # C:\Users\Clyde\Desktop\InterAutoTest_W\config
# 定义config.yml文件的路径
_config_file = _config_path + os.sep + "config.yml"
# print(_config_file)  # C:\Users\Clyde\Desktop\InterAutoTest_W\config\config.yml
# 定义log文件路径
_log_path = BASE_DIR + os.sep + "logs"


def get_config_path():
    '''返回config目录路径'''
    return _config_path


def get_config_file():
    '''返回config.yml文件路径'''
    return _config_file


def get_log_path():
    '''获取log文件路径'''
    return _log_path


# 读取配置文件
# 创建类
class ConfigYaml:
    def __init__(self):
        self.__config = YamlReader(get_config_file()).data()

    # 定义方法获取需要的信息
    def get_conf_url(self):
        return self.__config['BASE']['test']['url']

    def get_config_log_level(self):
        '''获取日志等级'''
        return self.__config["BASE"]['log_level']

    def get_config_log_extension(self):
        '''获取日志文件后缀'''
        return self.__config['BASE']['log_extension']


if __name__ == '__main__':
    # print(ConfigYaml().get_conf_url())
    print(ConfigYaml().get_config_log_level())
    print(ConfigYaml().get_config_log_extension())
