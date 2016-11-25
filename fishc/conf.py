#!/usr/bin/python
# -*- coding: UTF-8 -*-
#author renyuan  2016/4/11
from pymongo import MongoClient
CONN_ADDR1 = "dds-bp16f0f2258898941.mongodb.rds.aliyuncs.com:3717"
CONN_ADDR2 = "dds-bp16f0f2258898942.mongodb.rds.aliyuncs.com:3717"
REPLICAT_SET = "mgset-1181543"
username = "root"
password = "ClickPlus123456"
solr_url_update="http://120.27.146.30:8983/solr/good_1047/update?wt=json"
solr_url_delete="http://120.27.146.30:8983/solr/good_1047/update"
solr_url_query="http://120.27.146.30:8983/solr/good_1047/select?q="
client = MongoClient([CONN_ADDR1, CONN_ADDR2], replicaSet=REPLICAT_SET)
# #授权. 这里的user基于admin数据库授权
client.admin.authenticate(username, password)
test=client.test
goods=test.goods_1047
source=test.source_1047
nexus=test.nexus_1047
active=test.active_1047
mai6go_url="https://api.gou.com/OpenAPI/Goods/PriceInfo.do"
mai6go_total_url="https://api.gou.com/content/api/clickplus/data_goods.html"
appid="heICrCw4Q1+aeRvCstpHU0dQnYiCxGQn"
secrect_key="d09b8952e5706d20dba682187f698cc8"
ver="v1.0"
# client = MongoClient('114.55.228.9', 27017)#比较常用
# test=client.test                                      #test为mongo的db
# source=test.source_1047
# goods=test.goods_1047
# nexus=test.nexus_1047
# active=test.active_1047
