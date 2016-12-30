#!/bin/bash
cd /var/log
grep 'Failed password' auth.log|grep  invalid|awk '{print $11"\t" $13}'|grep -v Failed>>/alidata/zabbix/ssh_auth/txt/auth.log
grep 'Failed password' auth.log|grep -v invalid|awk '{print $9"\t" $11}'|grep -v Failed>>/alidata/zabbix/ssh_auth/txt/auth.log


grep 'Failed password' auth.log.1|grep  invalid|awk '{print $11"\t" $13}'|grep -v Failed>>/alidata/zabbix/ssh_auth/txt/auth.log.1
grep 'Failed password' auth.log.1|grep -v invalid|awk '{print $9"\t" $11}'|grep -v Failed>>/alidata/zabbix/ssh_auth/txt/auth.log.1

zgrep -a 'Failed password' auth.log.2.gz |grep invalid|awk '{print $11"\t"$13}'|grep -v Failed>>/alidata/zabbix/ssh_auth/txt/auth.log.2
zgrep -a 'Failed password' auth.log.2.gz |grep -v invalid|awk '{print $9"\t"$11}'|grep -v Failed>>/alidata/zabbix/ssh_auth/txt/auth.log.2 

zgrep -a 'Failed password' auth.log.3.gz |grep invalid|awk '{print $11"\t"$13}'|grep -v Failed>>/alidata/zabbix/ssh_auth/txt/auth.log.3
zgrep -a 'Failed password' auth.log.3.gz |grep invalid|awk '{print $11"\t"$13}'|grep -v Failed>>/alidata/zabbix/ssh_auth/txt/auth.log.3
cd /alidata/zabbix/ssh_auth/txt;cat auth.log*>>135ssh.txt
