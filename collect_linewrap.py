# By 憨憨羊の宇航鸽鸽
import json

file = open(input("strings.json: ").replace("\\","/"), 'r', encoding='utf-8')
fpa = json.loads(file.read())["Strings"]
file.close()
result = {}

a = 0
for line in fpa:
	if ("\n" in line):
		result[str(a)] = line
	a += 1

fp = open(r"linewrap.json", 'w', encoding='utf-8')
fp.write(json.dumps(result, indent=4, ensure_ascii=False))
fp.close()