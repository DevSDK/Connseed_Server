
'''
4hex 거르고 8hex float로
4hex 거르고 8hex float로
4hex 거르고 4hex int로
4hex 거르고 4hex int로
4hex 거르고 8hex float로
'''

import struct
import sqlite3
import threading

import requests
from xml.dom import minidom

baseaddress = "http://169.56.126.151"

id = 'sdkadmin'
pw = 'loginadmin'

loginresponse = requests.post(baseaddress + '/login', data={'id' : id, 'pw' : pw})

print(loginresponse.text)

if loginresponse.status_code is not 200:
    exit(0)

logincookie = loginresponse.cookies;



def run():
    threading.Timer(10.0, run).start()
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute("select id, EUI from Data_loradevice")
    rows = cur.fetchall()
    try:
        for row in rows:
            URL = 'https://thingplugpf.sktiot.com:9443/0240771000000174/v1_0/remoteCSE-00000174d02544fffef0'+row[1]+'/container-LoRa/latest'
            headers = { 'X-M2M-RI': '00000174d02544fffef0'+row[1]+'_0002', 'X-M2M-Origin': '00000174d02544fffef0'+row[1] , 'ukey' : 'STRqQWE5a28zTlJ0QWQ0d0JyZVlBL1lWTkxCOFlTYm4raE5uSXJKTC95eG9NeUxoS3d4ejY2RWVIYStlQkhNSA==' }

            response = requests.get(URL, headers = headers)

            if response.status_code == 200:
                xml = minidom.parseString(response.text)
                data = xml.getElementsByTagName("con")[0].firstChild.data

                tmpHex = data[4:12]
                humHex = data[16:24]
                luxHex = data[28:32]
                wtrHex = data[36:40]
                ppmHex = data[44:52]

                tmp = struct.unpack('!f', bytes.fromhex(tmpHex))[0]
                hum = struct.unpack('!f', bytes.fromhex(humHex))[0]
                lux = int(luxHex,16)
                wtr = int(wtrHex,16)
                ppm = struct.unpack('!f', bytes.fromhex(ppmHex))[0]

                URL = baseaddress+'/data/postrawdata'
                reqdata = {'device':row[0], 'wtr' : wtr, 'ppm' : ppm, 'tmp' : tmp, 'hum':hum, 'lux':lux}
                re = requests.post(URL, data = reqdata, cookies = logincookie)
                print( 'data send: '+ re.text + '  data : '+ reqdata.__str__())
    except Exception as e:
        print(e)
    conn.close()
run()