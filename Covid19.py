import requests
import time


# Code for Line Notification
url = 'https://notify-api.line.me/api/notify'
# token = 'HpXwfTCIngXaZSkwtM27S26girdn9MzGdOWbFUc793h'   # Token from Line Notify (Line Notify)
token = 'VmkcmkKUxIj653YwNtc1RAKQuaSLvTw0BKJEwIh3v1R ' #ตัวฉันอีกคน
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+ token}




f = open("date.txt", "r")
LastUpdate = f.read()
print('Last Update in text file : '+LastUpdate)

r = requests.get('https://covid19.th-stat.com/api/open/today')
print("LastUpdate",r.json()["UpdateDate"])
UpdateDate = r.json()["UpdateDate"]
print("Confirmed",r.json()["Confirmed"])
print("NewConfirmed",r.json()["NewConfirmed"])
print("NewRecovered",r.json()["NewRecovered"])
print("NewDeaths",r.json()["NewDeaths"])

msg = "อัพเดทข้อมูลล่าสุด: " + str(r.json()['UpdateDate'])
msg2 = " ติดเชื้อสะสม: " + str(r.json()['Confirmed'])
msg3 = " ติดเชื้อใหม่: " + str(r.json()['NewConfirmed'])
msg4 = " รักษาแล้ว: " + str(r.json()['NewRecovered'])
msg5 = " ตาย: " + str(r.json()['NewDeaths'])
msgall = msg+msg2+msg3+msg4+msg5

if LastUpdate != UpdateDate:
    r6 = requests.post(url, headers=headers, data = {'message':msgall})
    LastUpdate = UpdateDate
    f = open("date.txt", "w")
    f.write(str(LastUpdate))
    f.close()


#From https://www.youtube.com/watch?v=KXH9KroXl5Y