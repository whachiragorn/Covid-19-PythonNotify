import requests
r = requests.get('https://covid19.th-stat.com/api/open/today')
print("LastUpdate",r.json()["UpdateDate"])
print("Confirmed",r.json()["Confirmed"])
print("NewConfirmed",r.json()["NewConfirmed"])
print("NewRecovered",r.json()["NewRecovered"])
print("NewDeaths",r.json()["NewDeaths"])


# Code for Line Notification
url = 'https://notify-api.line.me/api/notify'
token = 'HpXwfTCIngXaZSkwtM27S26girdn9MzGdOWbFUc793h'   # Token from Line Notify
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+ token}

msg = "อัพเดทข้อมูลล่าสุด: " + str(r.json()['UpdateDate'])
msg2 = " ติดเชื้อสะสม: " + str(r.json()['Confirmed'])
msg3 = " ติดเชื้อใหม่: " + str(r.json()['NewConfirmed'])
msg4 = " รักษาแล้ว: " + str(r.json()['NewRecovered'])
msg5 = " ตาย: " + str(r.json()['NewDeaths'])
msgall = msg+msg2+msg3+msg4+msg5

#r1 = requests.post(url, headers=headers, data = {'message':msg})
#r2 = requests.post(url, headers=headers, data = {'message':msg2})
#r3 = requests.post(url, headers=headers, data = {'message':msg3})
#r4 = requests.post(url, headers=headers, data = {'message':msg4})
#r5 = requests.post(url, headers=headers, data = {'message':msg5})

r6 = requests.post(url, headers=headers, data = {'message':msgall})

#From https://www.youtube.com/watch?v=KXH9KroXl5Y
