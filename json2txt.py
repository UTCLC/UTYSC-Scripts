# By 天机Ceyase
import json
import requests
fpa = open(r"strings.txt", 'r', encoding='utf-8')
res = ""

print("正在下载：星号文本")
req = requests.get(r"")
Asterisk = json.loads(req.text)
print("正在下载：描述文本")
req = requests.get(r"")
PoundAsterisk = json.loads(req.text)
print("正在下载：其他文本")
req = requests.get(r"")
Filrted = json.loads(req.text)

a = 1
for line in fpa:
    if str(a) in Asterisk.keys():
        res += Asterisk[str(a)] + '\n'
    elif str(a) in PoundAsterisk.keys():
        res += PoundAsterisk[str(a)] + '\n'
    elif str(a) in Filrted.keys():
        res += Filrted[str(a)] + '\n'
    else:
        res += line
    a += 1
fpa.close()

fp = open(r"strings_after.txt", 'w', encoding='utf-8')
fp.write(res)
fp.close()