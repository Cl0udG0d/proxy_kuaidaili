# -*- coding: cp936 -*-
import time
from fake_useragent import UserAgent
import requests
import urllib2
from bs4 import BeautifulSoup
import sys


def headers_pool():
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    return headers

def check_url(url):
    req = urllib2.Request(url, headers=headers_pool())
    try:
        return urllib2.urlopen(req)
    except urllib2.URLError:
        pass
    
def kuaidaili_url():
    url= "https://www.kuaidaili.com/free/inha/"
    for i in range(1, 10):
        time.sleep(5)
        new_url = url+ str(i)
        rep=check_url(new_url)
        if rep!=None:
            kuaidaili_catch_ip(rep)
            
def output(ip, port, web_type):
    if (check_IP(str(ip + ":" + port), web_type)):
        sys.stdout.write(str(web_type).lower() + "://" + str(ip) + ":" + str(port) + "\n")
        f=open('ips.txt','a')
        f.write(str(web_type).lower()+"://"+str(ip+":"+port)+"\n")
        
def kuaidaili_catch_ip(rep):
    soup=BeautifulSoup(rep.read(),'lxml')
    tr_list=soup.find_all('tr')[1:]
    for tr in tr_list:
        td_list=tr.find_all('td')
        output(td_list[0].text,td_list[1].text,td_list[3].text)
        
def check_IP(ip, http_type):
    proxy_ip = {http_type: ip}
    result = requests.get("http://www.baidu.com", headers=headers_pool(), proxies=proxy_ip)
    if result.status_code == 200:
        return True
    else:
        return False

def main():
    kuaidaili_url()

if __name__=='__main__':
    main()
