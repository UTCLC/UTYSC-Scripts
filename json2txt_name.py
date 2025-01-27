# By 憨憨羊の宇航鸽鸽 基于 天机Ceyase
import json
import requests

def Replace(str_, name, result):
	print("在“"+str_+"”中发现了“"+name+"”，已替换为“"+result+"”\n结果为“"+str_.replace(name, result)+"”")
	return str_.replace(name, result)
def ReplaceName(str_, Names, Names_en):
	for name in Names_en.keys():
		result = ""
		if (Names[name].startswith("$")):
			result = Names[name].lstrip("$")
		else:
			for chr in Names[name]:
				result += chr + " "#加上字间空格
			result = result.strip(" ")#清除结尾多余的空格
			result = result.replace(" # ","#")#清除#左右的空格
		if (result != ""):
			if ("*  "+name in str_):
				str_ = Replace(str_, "*  "+name, "*  "+result)#星号开头
			if ("*  "+name.upper() in str_):
				str_ = Replace(str_, "*  "+name.upper(), "*  "+result)#星号开头且全大写
			if (" "+name+" " in str_):
				str_ = Replace(str_, " "+name+" ", " "+result+" ")#左右空格
			if (" "+name.lower()+" " in str_):
				str_ = Replace(str_, " "+name.lower()+" ", " "+result+" ")#左右空格且全小写 Flowey战出现
			if (" "+name.upper()+" " in str_):
				str_ = Replace(str_, " "+name.upper()+" ", " "+result+" ")#左右空格且全大写
			if (str_.startswith(name+" ")):
				str_ = Replace(str_, name+" ", result+" ")#右空格且句首
			if (str_.startswith(name.upper()+" ")):
				str_ = Replace(str_, name.upper()+" ", result+" ")#右空格且句首且全大写
			if (str_.endswith(" "+name) or (" "+name+"\n" in str_)):
				str_ = Replace(str_, " "+name, " "+result)#左空格且句尾
			if (str_.endswith(" "+name.upper()) or (" "+name.upper()+"\n" in str_)):
				str_ = Replace(str_, " "+name.upper(), " "+result)#左空格且句尾且全大写
			if (name+"#" in str_):
				str_ = Replace(str_, name+"#", result+"#")#右换行
			if (name.upper()+"#" in str_):
				str_ = Replace(str_, name.upper()+"#", result+"#")#右换行且全大写
			if ("#"+name in str_):
				str_ = Replace(str_, "#"+name, "#"+result)#左换行
			if ("#"+name.upper() in str_):
				str_ = Replace(str_, "#"+name.upper(), "#"+result)#左换行且全大写
			if ("，"+name in str_):
				str_ = Replace(str_, "，"+name, "，"+result)#左侧有逗号
			if ("，"+name.upper() in str_):
				str_ = Replace(str_, "，"+name.upper(), "，"+result)#左侧有逗号且全大写
			if (name+"，" in str_):
				str_ = Replace(str_, name+"，", result+"，")#右侧有逗号
			if (name.upper()+"，" in str_):
				str_ = Replace(str_, name.upper()+"，", result+"，")#右侧有逗号且全大写
			if (name+"。" in str_):
				str_ = Replace(str_, name+"。", result+"。")#右侧有句号
			if (name.upper()+"。" in str_):
				str_ = Replace(str_, name.upper()+"。", result+"。")#右侧有句号且全大写
			if (name+"!" in str_):
				str_ = Replace(str_, name+"!", result+"!")#右侧有叹号
			if (name.upper()+"!" in str_):
				str_ = Replace(str_, name.upper()+"!", result+"!")#右侧有叹号且全大写
			if (name+"！" in str_):
				str_ = Replace(str_, name+"！", result+"！")#右侧有全角叹号
			if (name.upper()+"！" in str_):
				str_ = Replace(str_, name.upper()+"！", result+"！")#右侧有全角叹号且全大写
			if (name+"?" in str_):
				str_ = Replace(str_, name+"?", result+"?")#右侧有问号
			if (name.upper()+"?" in str_):
				str_ = Replace(str_, name.upper()+"?", result+"?")#右侧有问号且全大写
			if (name+"？" in str_):
				str_ = Replace(str_, name+"？", result+"？")#右侧有全角问号
			if (name.upper()+"？" in str_):
				str_ = Replace(str_, name.upper()+"？", result+"？")#右侧有全角问号且全大写
			if ("："+name in str_):
				str_ = Replace(str_, "："+name, "："+result)#左侧有冒号
			if ("："+name.upper() in str_):
				str_ = Replace(str_, "："+name.upper(), "："+result)#左侧有冒号且全大写
			if ("■"+name in str_):
				str_ = Replace(str_, "■"+name, "■"+result)#左侧占位符
			if ("■"+name.upper() in str_):
				str_ = Replace(str_, "■"+name.upper(), "■"+result)#左侧占位符且全大写
			if (name+"■" in str_):
				str_ = Replace(str_, name+"■", result+"■")#右侧占位符
			if (name.upper()+"■" in str_):
				str_ = Replace(str_, name.upper()+"■", result+"■")#右侧占位符且全大写
			if ("▲"+name in str_):
				str_ = Replace(str_, "▲"+name, "▲"+result)#左侧占位符
			if ("▲"+name.upper() in str_):
				str_ = Replace(str_, "▲"+name.upper(), "▲"+result)#左侧占位符且全大写
			if (name+"▲" in str_):
				str_ = Replace(str_, name+"▲", result+"▲")#右侧占位符
			if (name.upper()+"▲" in str_):
				str_ = Replace(str_, name.upper()+"▲", result+"▲")#右侧占位符且全大写
			if ("▼"+name in str_):
				str_ = Replace(str_, "▼"+name, "▼"+result)#左侧占位符
			if ("▼"+name.upper() in str_):
				str_ = Replace(str_, "▼"+name.upper(), "▼"+result)#左侧占位符且全大写
			if (name+"▼" in str_):
				str_ = Replace(str_, name+"▼", result+"▼")#右侧占位符
			if (name.upper()+"▼" in str_):
				str_ = Replace(str_, name.upper()+"▼", result+"▼")#右侧占位符且全大写
			if ("●"+name in str_):
				str_ = Replace(str_, "●"+name, "●"+result)#左侧占位符
			if ("●"+name.upper() in str_):
				str_ = Replace(str_, "●"+name.upper(), "●"+result)#左侧占位符且全大写
			if (name+"●" in str_):
				str_ = Replace(str_, name+"●", result+"●")#右侧占位符
			if (name.upper()+"●" in str_):
				str_ = Replace(str_, name.upper()+"●", result+"●")#右侧占位符且全大写
			if (name+"..." in str_):
				str_ = Replace(str_, name+"...", result+"...")#右侧省略号
			if (name.upper()+"..." in str_):
				str_ = Replace(str_, name.upper()+"...", result+"...")#右侧省略号且全大写
			#if (name.upper() in str_):
				#str_ = Replace(str_, name.upper(), result)#全大写
			#if (name in str_):
				#str_ = Replace(str_, name, result)#直接替换
			#if (name in str_ and name == "Clover"):
				#str_ = Replace(str_, name, result)#Clover直接替换
			if (str_ == name):
				str_ = Replace(str_, name, result)#完全一致
			if (str_ == name.upper()):
				str_ = Replace(str_, name.upper(), result)#完全一致且全大写
	return str_

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
print("正在下载：人名文本")
req = requests.get(r"")
Names = json.loads(req.text)
req = requests.get(r"")
Names_en = json.loads(req.text)

a = 1
for line in fpa:
	if str(a) in Asterisk.keys():
		res += ReplaceName(Asterisk[str(a)], Names, Names_en) + '\n'
	elif str(a) in PoundAsterisk.keys():
		res += ReplaceName(PoundAsterisk[str(a)], Names, Names_en) + '\n'
	elif str(a) in Filrted.keys():
		res += ReplaceName(Filrted[str(a)], Names, Names_en) + '\n'
	else:
		res += ReplaceName(line, Names, Names_en)
	a += 1
fpa.close()

fp = open(r"strings_names.txt", 'w', encoding='utf-8')
fp.write(res)
fp.close()