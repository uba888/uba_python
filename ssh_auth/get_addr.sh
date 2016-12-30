#!/bin/bash

while read ip
do
	ipz=`echo $ip|awk '{print $3}'`
	addr=`./ip_addr.py $ipz`
	echo "$ip    $addr">>finally/$1
done<txt/$1

