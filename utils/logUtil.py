import datetime
import logging
from config.Config import *

# 定义日志级别的映射
log_l = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR
}


# 创建类
class Logger():
    def __init__(self, log_file, log_name, log_level):
        '''
        :param log_file: 输出文件名称
        :param log_name: Loggername
        :param log_level: 日志级别
        '''
        self.log_file = log_file
        self.log_name = log_name
        self.log_level = log_level

        # 设置logger名称
        self.logger = logging.getLogger(self.log_name)

        # 设置log级别
        self.logger.setLevel(log_l[self.log_level])

        # 定义输出格式
        formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
        if not self.logger.handlers:
            # 输出到文件
            fh_file = logging.FileHandler(log_file, encoding='utf-8')
            fh_file.setLevel(log_l[self.log_level])
            fh_file.setFormatter(formatter)

            # 输出到终端
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(log_l[self.log_level])
            fh_stream.setFormatter(formatter)

            # 添加handler
            self.logger.addHandler(fh_file)
            self.logger.addHandler(fh_stream)


# 日志文件名称 = logs目录 + 当前日期 + 扩展名
# 日志目录
log_path = get_log_path()
# 当前时间
current_time = datetime.datetime.now().strftime("%Y-%m-%d")
# 扩展名
log_extension = ConfigYaml().get_config_log_extension()
# 日志文件路径
log_file = os.path.join(log_path, current_time + log_extension)

# 日志级别
log_level = ConfigYaml().get_config_log_level()


# 对外提供方法使用
def my_log(log_name=__file__):
    return Logger(log_file=log_file, log_name=log_name, log_level=log_level).logger


if __name__ == '__main__':
    my_log().debug("this is debug")
