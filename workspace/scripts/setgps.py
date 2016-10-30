#-*- coding: utf-8 -*-
#windows: chcp 65001を実行
import sys
import io
import csv

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# DEMO用 移動するボタンをクリックするごとにGPS値を設定する
# 引数をpath番号として与える
# 初期化
with open('./data/gps.csv', 'w', newline='', encoding='utf-8') as fw:
  fw.write("")

# pathを取得
argv = sys.argv
path_index = int(argv[1])
with open('./data/path.csv', newline='', encoding='utf-8') as f:
  reader = csv.reader(f, delimiter=',', quotechar='|')
  for i, row in enumerate(reader):
      if i==path_index:
          with open('./data/gps.csv', 'w', newline='', encoding='utf-8') as fw:
              fw.write("緯度,経度\n")
              fw.write(row[0]+","+row[1])

# 実装用
