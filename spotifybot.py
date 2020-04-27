import requests,json



r1 = requests.get("https://accounts.spotify.com/en/login")



csrf_token = r1.cookies.get('csrf_token')




cookies = {"__bon" : "MHwwfDM4MzMwODk2NXwxNjA5ODk3NjUzMHwxfDF8MXwx",
               "csrf_token" : csrf_token,
               }

headers =  {"Accept" : "application/json, text/plain",
               "Content-Type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36",
"Connection" :	"keep-alive"
               }

data = {"remember" : "true",
            "username" : 'michael.beline@gmx.de',
            "password" : 'belka999',
            "csrf_token": csrf_token
            }



r2 = requests.post("https://accounts.spotify.com/api/login" ,data=data ,headers=headers, cookies=cookies)
print(f"login {r2.status_code}")
print(r2.text)

headers = {
"Connection":	"keep-alive",
"User-Agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"
}



cookies = {
    "_fbp":	"fb.1.1585846795569.1660036885",
     "_ga":	"GA1.2.1615050199.1585846794",
"ga_S35RN5WNT2": "GS1.1.1585949354.7.1.1585949367.0",
"_gcl_au":	"1.1.1541204063.1585846794",
"_gid":	"GA1.2.1424453668.1585846795",
"_hjid":	"7e55d60f-0eb6-4fdf-9086-8f05ad65524f",
"_scid":	"a54fa9b5-5e5e-4007-8e5b-2045260f49e2",
"cookieNotice":	"1",
"sp_adid" :   "d855e7da-78e0-482c-9c66-db2b03b0cc12",
"sp_dc": "AQAUK9OBog3Yn2GPNFhXiA0wCYC6xrYRH8bVH1FXv9WmVmoolY2toPhinC3X97ITgsO1r1omSJv6HGGyNSSNPrTOWqRNrfHumBQBrKllrPE",
"sp_gaid":	"0088fc73cb1494b5da3d5dfa77367e5b0f1e4915ca743cf85cf218",
"sp_key" :"9323a61d-5dfc-4a52-8e39-fd5eee2f9230",
"__bon" : "MHwwfDM4MzMwODk2NXwxNjA5ODk3NjUzMHwxfDF8MXwx",
               "csrf_token" : csrf_token,
}

r5=requests.get("https://open.spotify.com/get_access_token?reason=transport&productType=web_player",cookies=cookies,headers=headers)
print(r5.text)
r5_dict = json.loads(r5.text)
accessToken = r5_dict["accessToken"]




r6=requests.get("https://open.spotify.com/",cookies=cookies,headers=headers,timeout=10)






headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization':"Bearer "+ accessToken,
     "User-Agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:74.0) Gecko/20100101 Firefox/74.0"
}


response = requests.get('https://api.spotify.com/v1/me/player/devices', headers=headers,cookies=cookies)
print(response.text)

