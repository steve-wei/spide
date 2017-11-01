#!/usr/bin/env python
#coding:utf-8

import urllib2
import urllib
import re
import os


class Spider(object):

    def __init__(self):
        self.url = 'https://www.haha.mx/topic/5732/new/%s'
        self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
    #1、访问网页地址，获取网页源代码
    def get_page(self,page_index):

        headers = {'User-Agent': self.user_agent}
        try:
            request = urllib2.Request(url=self.url%str(page_index), headers=headers)
            response = urllib2.urlopen(request)
            content = response.read()
            return content
        except urllib2.HTTPError as e:
            print(e)
            exit()
        except urllib2.URLError as e:
            print('网络无法访问')
            exit()
    #2、根据抓取的网页源代码，提取想要的数据
    def analysis(self,content):
        pattern = re.compile('<p class="word-wrap joke-main-content-text">(.*?)</p>',re.S)
        items = re.findall(pattern, content)
        return items
    #3、保存抓取的数据
    def save(self,items,path):
        for item in items:
            item = item.replace('&ldquo;','').replace('&rdquo;','\n').replace('<br />','\n')
            path = 'xiaohua'
            if not os.path.exists(path):
                os.makedirs(path)
            file_path = path+'/'+'funny'+'.txt'
            f = open(file_path,'a')
            f.writelines(item)
            f.writelines('\n')
            f.close()

    def run(self):
        print ('开始抓取内容了')
        for i in range(1, 9):
            content = self.get_page(i)
            items = self.analysis(content)
            self.save(items,'xiaohua')
        print ('内容抓取完了')


if __name__ == '__main__':
    spider = Spider()
    spider.run()



