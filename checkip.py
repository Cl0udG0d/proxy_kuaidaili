# -*- coding: cp936 -*-
import json
import re
import requests

pattern1=re.compile('.*[https]')
pattern2=re.compile('\d+\.\d+\.\d+\.\d+')
pattern3=re.compile('\d+$')
with open('ip.json','r') as openfile:
    for ip_str in openfile:
        ip_dic=json.loads(ip_str)
        for i in ip_dic.values():
            proxytype=re.search(pattern1,str(i))
            proxyip=re.search(pattern2,str(i))
            proxyport=re.search(pattern3,str(i))
            testip=proxytype.group()+"://"+proxyip.group()+":"+proxyport.group()
            try:
                res = requests.get(url="http://icanhazip.com/",timeout=8,proxies={proxytype.group():testip})
                proxyIP = res.text
                if(proxyIP == testip):
                    print "this ip is good :"+"="*20+testip
                else:
                    print "this ip is not "
            except Exception,e:
                print "timeout"
