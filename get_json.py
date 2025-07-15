# By 憨憨羊の宇航鸽鸽
import json
import requests

def resolve(fpa, Asterisk, PoundAsterisk, Filrted, LineWrap, result, skipped, a, offset):
	if ("\n" in fpa[a + offset]):
		print(f"\\n found in {fpa[a + offset]}, affset {offset} + 1")
		if str(a + offset) in LineWrap.keys():
			result[a + offset] = LineWrap[str(a + offset)]
		else:
			result[a + offset] = fpa[a + offset]
		offset += 1
		result, skipped, a, offset = resolve(fpa, Asterisk, PoundAsterisk, Filrted, LineWrap, result, skipped, a, offset)
		a += 1
		return result, skipped, a, offset
	if str(a) in Asterisk.keys():
		if ((("_" in fpa[a + offset] or fpa[a + offset].lower() == fpa[a + offset]) and not " " in fpa[a + offset]) and not " " in Asterisk[str(a)] and not (Asterisk[str(a)] != "" and ord(Asterisk[str(a)][0]) > 256)):
			if (fpa[a + offset] != Asterisk[str(a)]):
				print("Skipped: " + fpa[a + offset] + " : " + Asterisk[str(a)])
				skipped[str(a)] = fpa[a + offset] + " : " + Asterisk[str(a)]
			result[a + offset] = fpa[a + offset]
		else:
			result[a + offset] = Asterisk[str(a)]
	elif str(a) in PoundAsterisk.keys():
		if ((("_" in fpa[a + offset] or fpa[a + offset].lower() == fpa[a + offset]) and not " " in fpa[a + offset]) or not " " in PoundAsterisk[str(a)] and not (PoundAsterisk[str(a)] != "" and ord(PoundAsterisk[str(a)][0]) > 256)):
			if (fpa[a + offset] != PoundAsterisk[str(a)]):
				print("Skipped: " + fpa[a + offset] + " : " + PoundAsterisk[str(a)])
				skipped[str(a)] = fpa[a + offset] + " : " + PoundAsterisk[str(a)]
			result[a + offset] = fpa[a + offset]
		else:
			result[a + offset] = PoundAsterisk[str(a)]
	elif str(a) in Filrted.keys():
		if ((("_" in fpa[a + offset] or fpa[a + offset].lower() == fpa[a + offset]) and not " " in fpa[a + offset]) and not " " in Filrted[str(a)] and not (Filrted[str(a)] != "" and ord(Filrted[str(a)][0]) > 256)):
			if (fpa[a + offset] != Filrted[str(a)]):
				print("Skipped: " + fpa[a + offset] + " : " + Filrted[str(a)])
				skipped[str(a)] = fpa[a + offset] + " : " + Filrted[str(a)]
			result[a + offset] = fpa[a + offset]
		else:
			result[a + offset] = Filrted[str(a)]
	else:
		result[a + offset] = fpa[a + offset]
	return result, skipped, a, offset

file = open(input("strings.json: ").replace("\\","/"), 'r', encoding='utf-8')
fpa = json.loads(file.read())["Strings"]
file.close()
result = [""] * (len(fpa) + 1)
skipped = {}

print("正在下载：星号文本")
req = requests.get(r"")
Asterisk = json.loads(req.text)
print("正在下载：描述文本")
req = requests.get(r"")
PoundAsterisk = json.loads(req.text)
print("正在下载：其他文本")
req = requests.get(r"")
Filrted = json.loads(req.text)
print("正在下载：带换行的文本")
req = requests.get(r"")
LineWrap = json.loads(req.text)

offset = -1
for a in range(0, len(fpa)):
	if (a + offset < len(fpa)):
		result, skipped, a, offset = resolve(fpa, Asterisk, PoundAsterisk, Filrted, LineWrap, result, skipped, a, offset)
		a += 1
if (result[-1] == result[-2] or result[-1] == ""):
	del result[-1]

fp = open(r"result.json", 'w', encoding='utf-8')
fp.write(json.dumps({"Strings": result}, indent=4, ensure_ascii=False))
fp.close()
fp = open(r"skipped.json", 'w', encoding='utf-8')
fp.write(json.dumps(skipped, indent=4, ensure_ascii=False))
fp.close()