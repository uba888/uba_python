function set_conf {
        #echo "##公司id:$1##站点id:$2##配置数据流---------------------------------------------------"
        #cd $conf_root
        #cp conf/SiteDb.properties conf/SiteDb.properties_bak
        sed -i "s/$/|$2,analytics_all,20,$1/g" conf
        #cat conf/SiteDb.properties
        #echo ">>>>>>修改配置完成，重启进程"
        #echo ">>>>>>旧进程"
        #ps aux | grep  WriteODPSYunAllinone|grep -v 'nurse'
        #kill -9 `ps aux | grep  WriteODPSYunAllinone|grep -v 'nurse'|gawk '{ print $2}'`
        #echo ">>>>>>新进程"
        #sleep 3
        #ps aux | grep WriteODPSYunAllinone|grep -v 'nurse'
        #echo ">>>>>>数据流配置完成........."
}
set_conf $2 $1 
