#-*- coding: utf-8 -*-
#windows: chcp 65001を実行
import sys
import io
import csv
import codecs
import math
from pyproj import Geod
import urllib.request
import os.path

# マップ出力
def download(url):
	img = urllib.request.urlopen(url)
	localfile = open( './app/assets/images/staticmap.png', 'wb')
	localfile.write(img.read())
	img.close()
	localfile.close()

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# pathを取得
location = []
with open('./data/gps.csv', newline='', encoding='utf-8') as f:
  reader = csv.reader(f, delimiter=',', quotechar='|')
  for i, row in enumerate(reader):
      location.append(row)

# print(location[1][0], location[1][1])

# get shelterlist
shelterlist = []
with open('./data/shelterlist.csv', newline='', encoding='utf-8') as f:
  reader = csv.reader(f, delimiter=',', quotechar='|')
  for i, row in enumerate(reader):
      shelterlist.append(row)

# print(shelterlist[1][3], shelterlist[1][4])

# 近傍のshelter計算
distance = []
p1_latitude = location[1][0]
p1_longitude = location[1][1]
obj_latitude = 0.0
obj_longitude = 0.0
obj_altitude = 0 # 単位は(m)
for i, row in enumerate(shelterlist):
    if i != 0:
        obj_latitude = row[3]
        obj_longitude = row[4]
        obj_altitude = 0 # 単位は(m)
        g = Geod(ellps='WGS84')
        azimuth, back_azimuth, distance_2d = g.inv(p1_longitude, p1_latitude, obj_longitude, obj_latitude)
        result = g.inv(p1_longitude, p1_latitude, obj_longitude, obj_latitude)
        # print (result)
        azimuth = result[0]
        back_azimuth = result[1]
        distance_2d = result[2]
        distance.append(distance_2d)

mindist = float("inf")
for i, dist in enumerate(distance):
    # print(dist)
    if mindist > dist:
        mindist = dist
        minindex = i

# print(minindex, distance[minindex])
# print(shelterlist[minindex+1])

# p1_latitude
# p1_longitude
obj_latitude = shelterlist[minindex+1][3]
obj_longitude = shelterlist[minindex+1][4]
# print (p1_latitude, p1_longitude, obj_latitude, obj_longitude)

# 地図と自己位置マーカー
# url = "https://maps.googleapis.com/maps/api/staticmap?center=34.687315,135.526201&size=640x480&sensor=false&zoom=14&markers=34.687315,135.526201&key=AIzaSyB62o5omyv9vrVo8Lwfm-Iq6FsNIMyfQ7I"

# 地図と自己位置マーカー青+避難所マーカー赤
#url = "https://maps.googleapis.com/maps/api/staticmap?center=34.687315,135.526201&size=640x480&sensor=false&zoom=14&markers=color%3Ablue%7Csize%3Anormal%7C34.687315%2C135.526201&markers=%7C34.688450%2C135.527450&path=color%3Ablue%7Cweight%3A12%7C34.687315%2C135.526201%7C34.688450%2C135.527450&key=AIzaSyB62o5omyv9vrVo8Lwfm-Iq6FsNIMyfQ7I"
# pathあり
# url = "https://maps.googleapis.com/maps/api/staticmap?center=" + str(p1_latitude) + "," + str(p1_longitude) \
#  + "&size=640x480&sensor=false&zoom=14&markers=color:blue|size:normal|" + str(p1_latitude) + "," + str(p1_longitude) \
#  + "&markers=" + str(obj_latitude)  + "," + str(obj_longitude) \
#  + "&path=color:blue|weight:12|" + str(p1_latitude) + "," + str(p1_longitude) \
#  + "|" + str(obj_latitude) + "," + str(obj_longitude) \
#  + "&key=AIzaSyB62o5omyv9vrVo8Lwfm-Iq6FsNIMyfQ7I"

# pathなし
url = "https://maps.googleapis.com/maps/api/staticmap?center=" + str(p1_latitude) + "," + str(p1_longitude) \
 + "&size=640x480&sensor=false&zoom=14&markers=color:blue|size:normal|" + str(p1_latitude) + "," + str(p1_longitude) \
 + "&markers=" + str(obj_latitude)  + "," + str(obj_longitude) \
 + "&key=AIzaSyB62o5omyv9vrVo8Lwfm-Iq6FsNIMyfQ7I"
# print (url)
download(url)

# 特定のshelterのsupplieslist_no.を取得
# ファイル名を返す
with open('./data/nearestshelter.txt' , 'w', newline='', encoding='utf-8') as f:
    f.write('supplieslist_' + str(minindex+1) + '.csv,'+str(minindex+1))
