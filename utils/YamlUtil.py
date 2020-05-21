import os
import yaml


# 创建类
class YamlReader:
    # 初始化
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('{yamlf}不存在'.format(yamlf=yamlf))
        self._data = None

    def data(self):
        '''yaml读取'''
        # 第一次调用data，读取yaml文档，如果不是，直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = yaml.safe_load(f)
                return self._data
        return self._data


if __name__ == "__main__":
    test_yaml = YamlReader('../testcase/t_yaml/data.yml')
    print(test_yaml.data())
