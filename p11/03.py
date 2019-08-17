# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 0017 15:20
# @Author  : Mat
# @Email   : 15092306271@163.com
# @File    : 03.py
# # @Software: PyCharm
from  xml.dom import  minidom



class Data:
    def __init__(self):
        self.dic = []

    def __getattr__(self, item):
        self.dic=[]
        with open('data.xml','r',encoding='utf-8')as f:
            dom = minidom.parse(f)
            root = dom.documentElement
            for j in ['el','p','l']:
                for i in root.getElementsByTagName(j):
                    if i.getAttribute(item):
                       self.dic.append(i.getAttribute(item))
                    else:
                        break

            return self.dic


