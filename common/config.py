# -*- coding: utf-8 -*-
# author = 'API'
#function:配置文件

try:
    import configparser  #python3的是ConfigParser
except:
    import ConfigParser as configparser #对应python2的是ConfigParser
from common.project_path import *

class DoConfig:
    def __init__(self,filenames):
        self.filenames=filenames
        self.cf=configparser.ConfigParser()
        self.cf.read(self.filenames,encoding="utf-8")

    def get_value(self,section,option):
        value=self.cf.get(section,option) # 片段 选项
        # value=cf[section][option]
        return value

if __name__=='__main__':
    t=DoConfig(conf_path)
    print(t.get_value('URL','url'))