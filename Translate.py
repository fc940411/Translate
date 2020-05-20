# encode:utf-8

import wx
import requests
import json
import re
from lxml import etree

class YoudaoFanyi(object):
    """爬取有道翻译"""

    def __init__(self, inputtext):
        self.session = requests.session()
        self.url = 'http://m.youdao.com/translate'
        self.headers = {'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}
        self.data = {'inputtext': inputtext, 'type': 'auto'}

    # def get_token(self):
    #     """获取token"""
    #     response = self.session.get(self.url)
    #     html_str = response.content.decode('utf8')
    #     token = re.findall(r"token: '(.*?)'", html_str)[0]
    #     self.data['token'] = token
    #     return self.data

    def lan_trans(self, url, data, headers):
        """发送请求，获取响应"""
        response = requests.post(url, data=data, headers=headers)
        return response.content.decode()

    def get_content(self, content):
        """提取译文"""
        html = etree.HTML(content)
        translation = html.xpath("//ul[@id='translateResult']/li/text()")
        if len(translation)>0:
            return translation[0]
        else:
            return '请输入正确的内容'

    def run(self):  # 实现主要逻辑
        # 1.检查输入的数据
        if self.data['inputtext']:
            # 2.发送请求，获取响应
            lan_trans = self.lan_trans(self.url, self.data, self.headers)
            # 3.提取译文
            content = self.get_content(lan_trans)
            return content
        else:
            return False


if __name__ == '__main__':
    inputtext = input("请输入要翻译的文本:")
    translate = YoudaoFanyi(inputtext)
    res = translate.run()
    print(res)