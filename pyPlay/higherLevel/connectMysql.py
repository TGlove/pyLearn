#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import mysql.connector
import time
try:
    #配置信息
    config={
        'host':'localhost',
        'port':3306,
        'user':'root',
        'password':'123456',
        'database':'text_1',
        'charset':'utf8'
    }
    #连接数据库
    # con=mysql.connector.connect(host='localhost',port=3306,user='root',
    #                         password='root',database='test',charset='utf8')
    con=mysql.connector.connect(**config)
    print con.connection_id
    print('success')
    time.sleep(5)
    #断开
    con.close()
except mysql.connector.Error,e:
    print e.message
    print 'fail'
