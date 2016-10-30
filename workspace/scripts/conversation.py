#-*- coding: utf-8 -*-
#windows: chcp 65001を実行
import sys
import io
import csv
import codecs
from goolabs import GoolabsAPI
import json
import os
import subprocess

sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# チャット画面で生成されたテキストファイルを読み込む
chat_text = ""
with open('./data/chat_text.txt', newline='', encoding='utf-8') as f:
    for row in f:
        chat_text = row
        print(row)

app_id = "13346dab6a67b41a884de45bcbf4bdc523ced4da711c35346f0a8501ef0b23fe"
api = GoolabsAPI(app_id)

echat_text = chat_text.encode('shift-jis')
uchat_text = echat_text.decode('shift-jis')
# # See sample response below.
# ret = api.entity(sentence=uchat_text)
# with open('./data/entity_response.json', 'w', newline='', encoding='utf-8') as f:
#   f.write(str(ret))

# See sample response below.
ret = api.morph(sentence=uchat_text)
with open('./data/morph_response.json', 'w', newline='', encoding='utf-8') as f:
    f.write(str(ret))
# print (json.dumps(ret, sort_keys = True, indent = 4))
# {'word_list': [[['トイレットペーパー', '名詞', 'トイレットペーパー'], \
# ['を', '格助詞', 'ヲ'], ['5', 'Number', 'ゴ'], ['個', '助数詞', 'コ'], \
# ['持', '動詞語幹', 'モ'], ['っ', '動詞活用語尾', 'ッ'], ['て', '動詞接尾辞', 'テ'], \
# ['い', '動詞語幹', 'イ'], ['く', '動詞接尾辞', 'ク'], ['よ', '終助詞', 'ヨ'], ['。', '句点', '＄']]], \
# 'request_id': 'labs.goo.ne.jp\t1477797716\t0'}

for i in ret:
    groupDict = ret[i]
    break
    
# print (groupDict[0][0][0])
# print (groupDict[0][0][1])
# print (groupDict[0][2][0])
# print (groupDict[0][2][1])

# pathを取得
argv = sys.argv
path_index = int(argv[1])

supplieslist = './data/supplieslist_' + str(path_index) + '.csv'
# path_indexのsupplieslistの更新
with open('dummy.csv', 'w', newline='', encoding='utf-8') as fw:
    writer = csv.writer(fw, delimiter=',', quotechar='|')
    with open(supplieslist, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=',', quotechar='|')
        for i, row in enumerate(reader):
            # print(i, row)
            if str(row[1]) == str(groupDict[0][0][0]):
                print(int(row[2]), int(groupDict[0][2][0]))
                rem = int(row[2]) - int(groupDict[0][2][0])
                row[2] = str(rem)
                print(str(rem))
            writer.writerow(row)

cmd = "cp -f dummy.csv " + supplieslist
# os.system(cmd)
ret  =  subprocess.check_call( cmd.split(" ") )
print (ret == 0)

cmd = "rm -f dummy.csv"
# os.system(cmd)
ret2  =  subprocess.check_call( cmd.split(" ") )
print (ret2 == 0)

chat_response = "ありがとうございます。避難所で待ってます。"
with open('./data/chat_response.txt', 'w', newline='', encoding='utf-8') as f:
    f.write(chat_response)
