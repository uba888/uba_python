#!/bin/bash 
ls -l txt/|awk '{print $9}'|sed  '1d'>ss
while read txt
do
	bash get_addr.sh $txt
done<ss
