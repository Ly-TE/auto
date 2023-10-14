# -*- coding: utf-8 -*-
# author = 'API'

import time
import logging
import logging.handlers
from common.project_path import *

class Log:
    def my_log(self,level,msg):
        #日志路径
        now=time.strftime('%Y-%m-%d_%H_%M_%S')
        new_log_path=log_dir+"/{0}.log".format(now[:10])

        #日志收集器
        mylog=logging.getLogger('test log')
        mylog.setLevel('DEBUG')

        #日志格式
        formatter=logging.Formatter('%(asctime)s-[%(levelname)s]-%(filename)s-%(name)s-日志信息:%(message)s')

        #输出到控制台
        sh=logging.StreamHandler()
        sh.setLevel('INFO')
        sh.setFormatter(formatter)

        #输出到文件
        fh=logging.FileHandler(new_log_path, encoding='utf-8') #指定编码方式
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        #对接
        mylog.addHandler(sh)
        mylog.addHandler(fh)

        if level=='debug':
            mylog.debug(msg)
        elif level=='info':
            mylog.info(msg)
        elif level=='error':
            mylog.error(msg)

        #移除
        mylog.removeHandler(sh)
        mylog.removeHandler(fh)

    @staticmethod
    def debug(msg):
        Log().my_log('debug',msg)

    @staticmethod
    def info(msg):
        Log().my_log('info',msg)

    @staticmethod
    def error(msg):
        Log().my_log('error',msg)

if __name__=='__main__':
    Log.debug('打印debug日志')
    Log.info('打印info日志')
    Log.error('打印error日志')