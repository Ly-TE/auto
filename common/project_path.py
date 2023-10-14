# -*- coding: utf-8 -*-
# author = 'API'

import os

#项目路径
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
#测试数据路径
data_path=os.path.join(project_path,'data','data.xlsx')
#配置路径
conf_path=os.path.join(project_path,'conf','online')
#生成测试报告路径
report_path=os.path.join(project_path,'report')
#生成日志路径
log_dir=os.path.join(project_path,'logs')
#要执行测试用例模块的路径
test_dir=os.path.join(project_path,'testcase')

if __name__=='__main__':
    print(project_path)
    print(data_path)
    print(conf_path)
    print(report_path)
    print(log_dir)
    print(test_dir)
