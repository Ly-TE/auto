# -*- coding: utf-8 -*-
# author = 'API'

import time
import unittest

import HTMLTestRunnerNew

from common.project_path import *

# from testcase import test_queryRole


# # 1:集成单个模块，调试用
# #加载
# loader=unittest.TestLoader()
# result=loader.loadTestsFromModule(test_queryRole)
# #集成
# suite=unittest.TestSuite()
# suite.addTest(result)


# 2：集成指定目录下所有测试模块
suite = unittest.defaultTestLoader.discover(test_dir,  # test_dir在project_path里
                                            pattern='test*.py',
                                            top_level_dir=None)

# 执行 生成报告
now = time.strftime('%Y-%m-%d_%H_%M_%S')
with open(report_path + '/' + now + '_Report.html', 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2, title='API_report')
    runner.run(suite)
