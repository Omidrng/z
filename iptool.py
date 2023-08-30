import requests
from time import sleep
import json
from fake_useragent import UserAgent

fake = UserAgent()

ip = (input("Enter IP/URL with out https/http: "))
ipcheck = f"http://ip-api.com/json/{ip}"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko','Pragma': 'no-cache','Accept': 'application/json'}
ipinfo = requests.get(ipcheck, headers=headers)
urll = "https://check-host.net/check-ping?host={0}&node=ir1.node.check-host.net&node=ir3.node.check-host.net&node=ir4.node.check-host.net"
urlhttp = f"https://check-host.net/check-http?host={ip}&node=ir1.node.check-host.net&node=ir3.node.check-host.net&node=ir4.node.check-host.net"
url = urll.format(ip)
myip = "https://api.ipify.org/?format=json"

reshttp = requests.get(urlhttp, headers=headers)
httptext = reshttp.text
httpjson = json.loads(httptext)
httpapi = (httpjson['request_id'])
url2http = f"https://check-host.net/check-result/{httpapi}"
sleep(3)
hosthttp = requests.get(url2http, headers=headers, timeout=4)
httpu = hosthttp.text
httpm = json.loads(httpu)
ir1http = httpm['ir1.node.check-host.net'][0][0]
ir2http = httpm['ir4.node.check-host.net'][0][0]
ir3http = httpm['ir3.node.check-host.net'][0][0]
a = "Tehran HTTP: ", ir1http,"Tabriz HTTP: ", ir2http, "Shiraz HTTP: ", ir3http

ipformat = "http://" + ip



checkurl = requests.get(ipformat, headers=headers)
a = checkurl.status_code
if a == 200:
        print("Status: success")
        sleep(1)
        print("Wait 15 secend to complete...")
        sleep(4)
        if ir1http == 1:
            print("Tehran HTTP: Ok")
        else:
            print("Tehran HTTP: TimeOut")
        sleep(4)
        if ir2http == 1:
            print("Tabriz HTTP: Ok")
        else:
            print("Tabriz HTTP: TimeOut")
        sleep(4)
        if ir3http == 1:
            print("Shiraz HTTP: Ok")
        else:
            print("Shiraz HTTP: TimeOut")



        res = requests.get(url, headers=headers)
        x = res.text
        z = json.loads(x)
        api = (z['request_id'])

        url2 = "https://check-host.net/check-result/{0}"
        realurl = url2.format(api)
        sleep(15)
        hostping = requests.get(realurl, headers=headers, timeout=4)
        u = hostping.text
        m = json.loads(u)

        realip = m['ir1.node.check-host.net'][0][0][2]
        ir1 = m['ir1.node.check-host.net'][0][0][0]
        ir2 = m['ir4.node.check-host.net'][0][0][0]
        ir3 = m['ir3.node.check-host.net'][0][0][0]



        a = "Tehran ping: ", ir1,"Tabriz ping: ", ir2, "Shiraz ping: ", ir3

        l = ipinfo.text
        n = json.loads(l)

        country = n['country']
        countrycode = n['countryCode']
        city = n['city']
        timezone = n['timezone']
        isp = n['isp']
        
        myipp = requests.get(myip)
        myipjson = myipp.text
        derf = json.loads(myipjson)
        zzz = derf['ip']
        myipcheck = f"http://ip-api.com/json/{zzz}"
        sds = requests.get(myipcheck, headers=headers)
        sws = sds.text
        moodi = json.loads(sws)
        myipcountry = moodi['country']
        myipcountrycode = moodi['countryCode']
        myipcity = moodi['city']
        myiptimezone = moodi['timezone']
        myipisp = moodi['isp']
        print("Your IP:", zzz)
        sleep(1)
        print("Your IP country:", myipcountry)
        sleep(1)
        print("Your IP country code:", myipcountrycode)
        sleep(1)
        print("Your IP city:", myipcity)
        sleep(1)
        print("Your IP time zone:", myiptimezone)
        sleep(1)
        print("Your IP ISP:", myipisp)
        sleep(1)
        print("IP address:", realip)
        sleep(1)
        print("Country:", country)
        sleep(1)
        print("CountryCode:", countrycode)
        sleep(1)
        print("City:", city)
        sleep(1)
        print("TimeZone:", timezone)
        sleep(1)
        print("ISP:", isp)
        sleep(1)


        if ir1 == "OK":
            print("Tehran ping: Ok")
        else:
            print("Tehran ping: TimeOut")
        sleep(1)
        if ir2 == "OK":
            print("Tabriz ping: Ok")
        else:
            print("Tabriz ping: TimeOut")
        sleep(1)
        if ir3 == "OK":
            print("Shiraz ping: Ok")
        else:
            print("Shiraz ping: TimeOut")
        sleep(1)

        




        if ir1 == "OK" and ir2 == "OK" and ir3 == "OK":
            print("IP clear")
        else:
            print("IP not clear")
        sleep(100)
else:
        print("IP/URL is filter please turn on proxy or VPN and try again")
        sleep(10)