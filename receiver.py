#! /usr/bin/env python

import requests, json, shutil

read_url = "http://192.168.1.117:5000/index"
picture_url = "http://192.168.1.117:5000/picture"
json_file = "default.json"

def get_picture(name):
    r = requests.post(picture_url, data={'name':name}, stream=True)
    if r.status_code == 200:
        with open(name + '.png', 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    
    print r.status_code, r.reason

def get_reads():
    id_list = []
    r = requests.post(read_url)
    if r.status_code == 200:
        with open(json_file, 'w') as f:
            f.write(r.text)
        read_list = json.loads(r.text)
        for read in read_list['RFID Data List']:
            id_list.append(str(read['ID Number']))
        return id_list

if __name__ == "__main__":
    rfid_list = get_reads()
    for tag in rfid_list:
        get_picture(tag)