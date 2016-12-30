#!/bin/bash
grep 'Failed password' /var/log/auth.log|awk '{print $(NF-3)}'|grep -v Failed|sort|uniq -c|sort -nr|awk '{print $2"="$1}'>/alidata/zabbix/ssh_auth/black.txt
Deny='5'
while read line
do
	ip=`echo $line|awk -F '=' '{print $1}'`
	num=`echo $line|awk -F '=' '{print $2}'`
	if [ $num -gt $Deny ];then
		echo q|sudo -C echo "sshd:$ip:deny">>/etc/hosts.deny
	fi
done</alidata/zabbix/ssh_auth/black.txt
