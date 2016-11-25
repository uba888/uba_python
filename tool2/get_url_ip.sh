#!/bin/bash
#echo $1
putip=`dig $1|grep $1|grep A|awk '{print $5}'|grep -v '^$'`
#echo $putip
curl "http://api.ip138.com/query/?ip=$putip&datatype=jsonp&callback=find" -H "token:4d977467f918b9c90b242ce0fc20b069"
echo ""
