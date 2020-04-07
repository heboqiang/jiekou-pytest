# coding:utf-8
# heboqiang



import  unittest
import  json
from base.method import Method,IsContent
from page.laGou import *
from page.diyi1 import *
from utils.public import *
from utils.operationExcel import OperationExcel
from utils.operationJson import OperationJson
import requests
requests.packages.urllib3.disable_warnings()
from common.db import *
from common.logger import Log
import pytest


'''下面封装了get，post，dubbo请求的测试用例'''


class Test_Pytest():
	# log = Log()
	def setup_class(self):
		print ('类前面')
		# 环境检查
		if check_user(sql="SELECT * FROM jp_user WHERE phone = '18821768014';"):
			del_user(sql="delete from jp_user where phone = '18821768014';")

	def teardown_class(self):
		print ('类之后')
		# 数据库断言
		# self.assertTrue (check_user (NOT_EXIST_USER))
		# 环境清理
		# del_user (NOT_EXIST_USER)c

	def setup_method(self):
		print ('方法前面')
		self.obj=Method()
		self.p=IsContent()
		self.execl=OperationExcel()
		self.operationJson=OperationJson()
		self.log = Log()

	def teardown_method(self):
		print ('方法后')

	def statusCode(self,r):
		assert r.status_code == 200
		print(r.status_code)

		# print(r.json()['code'])
		# self.assertEqual(r.json ()['code'], 200)

	def isContent(self,r,row):
		self.statusCode(r=r)
		assert self.p.isContent (row=row, str2=r.text)

	def test_one(self):
		print ("----start------")
		pytest.xfail (reason='该功能尚未完成')
		print ("test_one方法执行")
		assert 1 == 1

	@pytest.mark.xfail
	def test_one1(self):
		print ("test_one方法执行")
		assert 1 == 2

	# @pytest.mark.xfail
	def test_post_001(self):
		"""测试post接口-直接请求"""
		print ("test_laGou_001方法执行")
		self.log.info("------测试post接口-直接请求：start!---------")
		# print(check_user(user=jp_user,name=18821768014))
		"sign为空"
		r = self.obj.post(row=1,data=self.operationJson.getRequestsData(row=1))
		print ("test_laGou_001 is:", r.text)
		self.log.info("获取请求结果：%s" % r.text)
		self.isContent (r=r, row=1)
		self.execl.writeResult (1,'pass')

	@pytest.mark.xfail
	def test_post_002(self):
		print ("test_laGou_002方法执行")
		"测试post接口-参数化请求"
		self.log.info("------测试post接口-参数化请求：start!---------")
		r = self.obj.post(row=1,data=set_so_keyword1(phone='18821768014'))
		print ("test_laGou_002 is:", r.text)
		self.isContent (r=r, row=1)
		self.execl.writeResult (1,'pass')

	# def test_get_001(self):
	# 	'''测试get接口'''
	# 	r = self.obj.get(row=4,params=json.loads(self.operationJson.getRequestsData(4)))
	# 	print(type(json.loads(self.operationJson.getRequestsData(4))))
	# 	print(r.url)
	# 	self.isContent(r=r, row=4)
	# 	self.execl.writeResult(4, 'pass')
    #
	# def test_dubbo_003(self):
	# 	'''测试dubbo'''
	# 	r = self.obj.dubbo(row=5,param=self.operationJson.getRequestsData(5),method='tradeDetailQuery')
	# 	# print(type(json.loads(self.operationJson.getRequestsData(5))))
	# 	print (self.operationJson.getRequestsData(5))
	# 	print(r.text)
# print (set_so_keyword(app_id=20180829170725138653,sign='8C7DF610ECB03AEA0DA6AA64F6D8C572'))p_id=20180829170725138653,sign='8C7DF610ECB03AEA0DA6AA64F6D8C572'))


# if __name__=="__main__":
#     pytest.main(['-s','E:\qjj_interface_auto\\tests'])

