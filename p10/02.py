# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 0016 17:30
# @Author  : Mat
# @Email   : 15092306271@163.com
# @File    : 02.py
# @Software: PyCharm
import json



with open('data.json','r',encoding='utf8')as f:
    end = json.loads(f.read())


b={}
def func(src):
    if isinstance(src,dict):
        for k,v in src.items():
            if isinstance(v,int):
                b[k]=v
            elif isinstance(v,dict):
                func(v)
            else:
                if isinstance(v,list):
                    for i in v:
                        if not isinstance(i,int):
                            func(i)

func(end)
c={}
with open('p2.txt','w')as f:
    a = sorted(b.items(),key=lambda x:x[1],reverse=True)
    f.write(str(a))

