import requests


def requests_get(url, headers=None):
    """创建封装get方法"""
    # 发送requests get请求
    response = requests.get(url=url, headers=headers)
    # 获取结果响应内容
    code = response.status_code
    try:
        body = response.json()
    except Exception as e:
        body = response.text
    # 内容存到字典
    response_dict = dict()
    response_dict['code'] = code
    response_dict['body'] = body
    # 字典返回
    return response_dict


def requests_post(url, headers=None, data=None):
    """创建封装post方法"""
    # 发送requests post请求
    response = requests.post(url=url, headers=headers, json=data)
    # 获取结果响应内容
    code = response.status_code
    try:
        body = response.json()
    except Exception as e:
        body = response.text
    # 内容存到字典
    response_dict = dict()
    response_dict['code'] = code
    response_dict['body'] = body
    # 字典返回
    return response_dict


class RequestsApi():
    '''重构request类'''

    def request_api(self, url, json=None, headers=None, method='get', cookies=None, data=None):
        '''公共方法'''
        if method == 'get':
            response = requests.get(url=url, json=json, headers=headers, cookies=cookies, data=data)
        elif method == 'post':
            response = requests.post(url=url, json=json, headers=headers, cookies=cookies, data=data)

        # 获取结果响应内容
        code = response.status_code
        try:
            body = response.json()
        except Exception as e:
            body = response.text
        # 内容存到字典
        response_dict = dict()
        response_dict['code'] = code
        response_dict['body'] = body
        # 字典返回
        return response_dict

    def get(self, url, **kwargs):
        return self.request_api(url, **kwargs)

    def post(self, url, **kwargs):
        return self.request_api(url, method='post', **kwargs)
