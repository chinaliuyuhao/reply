#!/usr/bin/env python
# -*- coding: utf-8 -*-


#1：用Python的实现下载www.bluecore.com.cn的首页HTML。



import requrest
import re 
import pathlib
from pathlib import Path
import threading 



class Bluecore01:
  def __init__(self):
    self.url= 'http://www.bluecore.com.cn/'
    self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
          }
    
  def gain_html(self):
    # 获取网页源代码
    html = requests.get(url=self.url,headers = self.headers)
    html = html.text
    return html
  
  def save_url(self,html)
    #保存网页源代码
    with open('bluecore.html',dict):
      f.write(html.encode('utf-8'))
            print('写入成功')
        
        
        
   def save_style(self,html,dirt):
    #保存网页的样式和图片
        for k,y in dirt.items():
            path = re.compile('{}'.format(y))
            find_all = re.findall(path,html)
            for i in find_all:
                path = pathlib.Path('dist/{}'.format(k))
                if not path.exists():
                    path.mkdir(parents=True)
                url = self.url+'dist/{}/'.format(k)+i
                download = requests.get(url,headers =self.headers)
                with open("H:/bluecore/dist/{}/{}".format(k,Path(url).name),'wb')as f:
                    f.write(download.content)
                    print('{}---->写入成功'.format(Path(url).name))
                    
                    
    def bg_url(self):
        url =['http://www.bluecore.com.cn/dist/images/banner-bj.jpg','http://www.bluecore.com.cn/dist/images/box1-bj.png','http://www.bluecore.com.cn/dist/images/box1-icon.png',
              'http://www.bluecore.com.cn/dist/images/new-bj.jpeg']
        path = Path('H:/bluecore/dist/images/')
        if not path.exists():
            path.mkdir(parents=True)
        for i in url:
            p = Path(i).name
            response = requests.get(i,self.headers)
            with open('H:/bluecore/dist/images/{}'.format(p),'wb')as f:
                f.write(response.content)
                print('{}成功写入'.format(p))
                
                
                
if __name__ == '__main__':
    event = threading.Event()
    b = Bluecore01()
    html2 = b.gain_html()
    threading.Thread(target=b.get_url,args=(html2,event,)).run()
    if True:
        threading.Thread(target=b.save_style,args=(html2,{'images': '"dist/images/(.*?)"'})).run()
        threading.Thread(target=b.save_style,args=(html2,{'css' :'<link rel="stylesheet" href="dist/css/(.*?)\?.*?">'})).run()
        threading.Thread(target=b.save_style,args=(html2,{'js':'<script [type="text/javascript"]?.*?src="dist/js/(.*?)\?.*?"></script>'})).run()
        threading.Thread(target=b.save_style,args=(html2,{ 'font':'<link rel="stylesheet" href="dist/font/(.*?)">'})).run()
    threading.Thread(target=b.bg_url).run()


  
