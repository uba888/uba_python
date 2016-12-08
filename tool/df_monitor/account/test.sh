#!/bin/bash

while read domain
do
	#echo "普通页面域名：sl.$domain 指向：swanrov.b0.upaiyun.com dns记录类型：cname记录 "
	#echo "个性化域名：slg.$domain 指向114.55.4.124 dns记录类型：a记录"
	#echo " 活动跳转域名：slh.$domain 指向120.27.146.30  dns记录类型：a记录"
	#a=`dig $1.$domain +short|head -1`
	#if [ ! -n "$a" ];then
	#	echo $domain
	#else
	#	echo $a
	#fi
	#echo sl.$domain
	#echo http://slh.$domain      http://sl.$domain 		http://slg.$domain
	#mysql -h114.55.21.195 -ujdyun_ops -pJdyun123456 -e "use marketingcloud_business;insert into auto_tenant_url (tenant_id,url,type) values(1072,"\""http://slh.$domain"\"",1)"
	#mysql -h114.55.21.195 -ujdyun_ops -pJdyun123456 -e "use marketingcloud_business;insert into auto_tenant_url (tenant_id,url,type) values(1072,"\""http://sl.$domain"\"",0)"

	#mysql -h114.55.21.195 -ujdyun_ops -pJdyun123456 -e "use marketingcloud_business;update site set cdn_url="\""http://sl.$domain"\"",personalized_url="\""http://slg.$domain/"\"" where main_url="\""http://slh.$domain"\"";"

	bash set_conf.sh $domain

done< site
