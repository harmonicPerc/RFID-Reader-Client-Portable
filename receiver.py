#! /usr/bin/env python

# MIT License
# 
# Copyright (c) 2016 Ross Bunker
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import requests, json, shutil, os
from PIL import Image

# If portable_client is set to true, format_picture will take the smaller screen size
# into account when storing the image
portable_client = True
# Resolution of the portable touchscreen. Keep in mind that this is (columns, rows) and
# image sizes are given in (rows, columns)
portable_resolution = (800, 395) # True resolution is (800, 480), but the task bar uses some space
# max_thumbnail_size defines the largest dimensions acceptable for the image thumbnail
max_thumbnail_size = (200, 200)
# Urls for POST requests to httpserver
read_url = "http://192.168.1.117:5000/index"
picture_url = "http://192.168.1.117:5000/picture"
# Name that the retrieved JSON file will be stored as
json_file = "default.json"

# get_reads retrieves a JSON object containing EPCs and other information from all tags
# collected in the most recent read by the M6e xPRESS Sensor Hub. The full JSON object is
# stored, and a list containing only the EPC ids is returned
def get_reads():
    id_list = []
    r = requests.post(read_url)
    if r.status_code == 200:
        destination = os.path.join(os.getcwd(), 'database', json_file)
        with open(destination, 'w') as f:
            f.write(r.text)
        read_list = json.loads(r.text)
        for read in read_list['RFID Data List']:
            id_list.append(str(read['ID Number']))
        return id_list

# get_picture will retrieve a picture from the http server when passed an EPC id
def get_picture(name):
    destination = os.path.join(os.getcwd(), 'database', 'pictures', name) + '.png'
    if os.path.isfile(destination):
        print name, "already exists, skipping."
    else:
        r = requests.post(picture_url, data={'name':name}, stream=True)
        if r.status_code == 200:            
            with open(destination, 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)
        format_picture(name)
        print name, "status:", r.status_code, r.reason

# format_picture will resize the input picture to fit the screen, if necessary for the
# portable unit. It will also create a thumbnail image and store it with 'thumb' appended
# to the filename
def format_picture(name):
    original_image_location = os.path.join(os.getcwd(), 'database', 'pictures', name) + '.png'
    im = Image.open(original_image_location)

    if portable_client:
        if im.size[0] > portable_resolution[0] or im.size[1] > portable_resolution[1]:
            resize_ratio = min(portable_resolution[0]/float(im.size[0]), portable_resolution[1]/float(im.size[1]))
            im.thumbnail((im.size[0]*resize_ratio, im.size[1]*resize_ratio), Image.ANTIALIAS)
            im.save(original_image_location)

    thumbnail_location = os.path.join(os.getcwd(), 'database', 'pictures', name) + 'thumb.png'
    thumbnail_resize_ratio = min(max_thumbnail_size[1]/float(im.size[0]), max_thumbnail_size[0]/float(im.size[1]))
    im.thumbnail((im.size[0]*thumbnail_resize_ratio, im.size[1]*thumbnail_resize_ratio), Image.ANTIALIAS)
    im.save(thumbnail_location, 'PNG')

# Tag read information is retrieved from the server and used to also retrieve pictures
# associated with the tag reads. If the pictures already exist, no action is taken.
# Otherwise, the pictures are resized to fit onscreen if necessary, and a thumbnail is
# created.
if __name__ == "__main__":
    rfid_list = get_reads()
    for tag in rfid_list:
        get_picture(tag)
