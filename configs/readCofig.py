# coding:utf-8
#heboqiang

import os
import configparser

cur_path = os.path.dirname(os.path.relpath(__file__))
configpath  = os.path.join(cur_path,"cfg.ini")
conf = configparser.ConfigParser()
conf.read(configpath,encoding="utf-8")
# #开发环境
# host = conf.get('mysql_1','host')
# port = conf.get('mysql_1','port')
# user = conf.get('mysql_1','user')
# passwd = conf.get('mysql_1','passwd')
# db = conf.get('mysql_1','db')

# 测试环境
# url = conf.get('mysql_2','url')
# user = conf.get('mysql_2','user')
# passwd = conf.get('mysql_2','passwd')
# db = conf.get('mysql_2','db')

# # 预发布环境
url = conf.get('mysql_3','url')
host = conf.get('mysql_3','host')
user = conf.get('mysql_3','user')
passwd = conf.get('mysql_3','passwd')
db = conf.get('mysql_3','db')




# send_mail_1 = conf.get('email','send_mail')
# send_user_1 = conf.get('email','send_user')
# # login_1 = conf.get('email','login')
# to_user_1 = conf.get('email','to_user')
# send_mail_ren_1 = conf.get('email','send_mail_ren')


