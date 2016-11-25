#!/bin/bash

#usage: bash judge_domain.sh jump_url cdn_url personal_url

function verify {
	jump_url=`echo $1|awk -F '//' '{print $2}'`
	personal_url=`echo $3|awk -F '//' '{print $2}'`
	cdn_url=`echo $2|awk -F '//' '{print $2}'`
	echo "jump:`dig $jump_url +short`"
	echo "cdn:`dig $cdn_url +short|head -1`"
	echo "personal:`dig $personal_url +short`"
}

function nginx_config {
    ##nginx跳转配置 传入jump_url,personal_url
    echo "==================================nginx跳转配置============================================="
    jump_url=`echo $1|awk -F '//' '{print $2}'`
    personal_url=`echo $2|awk -F '//' '{print $2}'`
    jump_ip=`./getip.py $jump_url`
    echo ">>>>>>jump:$jump_ip进行配置并重启 sudo sh -c \"sed -s "s/alihuodong.clickplus.cn/$jump_url/g" nginx.conf>>/etc/nginx/conf.d/vhost.conf\""
    echo ">>>>>>personal进行配置并重启 sudo sh -c \"sed -s "s/allpersonal.clickplus.cn/$personal_url/g" nginx.conf>>/etc/nginx/conf.d/vhost.conf\""
    while true;do
        echo "=================================请选择相应菜单进行操作======================================="
        echo "请选择你要进行的操作:"
        echo " 1) 重启jump的nginx"
        echo " 2) 重启个性化的nginx"
        echo " q) exit"
        read num
        case "$num" in
            "1")
                ssh -t -p 22 ops@$jump_ip "bash /alidata/account/nginx_config.sh $jump_url";;
            "2")
                ssh -t -p 22 ops@114.55.4.124 "bash /alidata/account/nginx_config.sh $personal_url";;
            "q")
                echo "===退出菜单....."
                break;;
        esac
   	done
}

while true;do
	echo "===========请选择菜单==========="
	echo "1) 验证域名"
	echo "2) 进行nginx配置"
	echo "q) 退出"
	read num
	case $num in
		"1")
			verify $1 $2 $3;;		
		"2")
			nginx_config $1 $3;;
		"q")
			echo "退出菜单"
			break;;
	esac
done
