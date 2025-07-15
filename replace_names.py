# By SheepYhangCN
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
		if (result != "" and ("三 叶" not in str_)):
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
			if (str_.startswith(name+"\n")):
				str_ = Replace(str_, name+"\n", result+"\n")#右换行且句首
			if (str_.startswith(name.upper()+"\n")):
				str_ = Replace(str_, name.upper()+"\n", result+"\n")#右换行且句首且全大写
			if (str_.endswith("\n"+name) or ("\n"+name+"\n" in str_)):
				str_ = Replace(str_, "\n"+name, "\n"+result)#左换行且句尾
			if (str_.endswith("\n"+name.upper()) or ("\n"+name.upper()+"\n" in str_)):
				str_ = Replace(str_, "\n"+name.upper(), "\n"+result)#左换行且句尾且全大写
			if (str_.startswith(name+"#")):
				str_ = Replace(str_, name+"#", result+"#")#右换行且句首
			if (str_.startswith(name.upper()+"#")):
				str_ = Replace(str_, name.upper()+"#", result+"#")#右换行且句首且全大写
			if (str_.endswith("#"+name) or ("#"+name+"#" in str_)):
				str_ = Replace(str_, "#"+name, "#"+result)#左换行且句尾
			if (str_.endswith("#"+name.upper()) or ("#"+name.upper()+"#" in str_)):
				str_ = Replace(str_, "#"+name.upper(), "#"+result)#左换行且句尾且全大写
			# if (name+"#" in str_):
			# 	str_ = Replace(str_, name+"#", result+"#")#右换行
			# if (name.upper()+"#" in str_):
			# 	str_ = Replace(str_, name.upper()+"#", result+"#")#右换行且全大写
			# if ("#"+name in str_):
			# 	str_ = Replace(str_, "#"+name, "#"+result)#左换行
			# if ("#"+name.upper() in str_):
			# 	str_ = Replace(str_, "#"+name.upper(), "#"+result)#左换行且全大写
			# if (name+"\n" in str_):
			# 	str_ = Replace(str_, name+"\n", result+"\n")#右换行
			# if (name.upper()+"\n" in str_):
			# 	str_ = Replace(str_, name.upper()+"\n", result+"\n")#右换行且全大写
			# if ("\n"+name in str_):
			# 	str_ = Replace(str_, "\n"+name, "\n"+result)#左换行
			# if ("\n"+name.upper() in str_):
			# 	str_ = Replace(str_, "\n"+name.upper(), "\n"+result)#左换行且全大写
			if ("#"+name+"#" in str_):
				str_ = Replace(str_, "#"+name+"#", "#"+result+"#")#左右换行
			if ("\n"+name+"\n" in str_):
				str_ = Replace(str_, "\n"+name+"\n", "\n"+result+"\n")#左右换行
			if ("#"+name.upper()+"#" in str_):
				str_ = Replace(str_, "#"+name.upper()+"#", "#"+result+"#")#左右换行且全大写
			if ("\n"+name.upper()+"\n" in str_):
				str_ = Replace(str_, "\n"+name.upper()+"\n", "\n"+result+"\n")#左右换行且全大写
			if ("#"+name+" " in str_):
				str_ = Replace(str_, "#"+name+" ", "#"+result+" ")#左换行右空格
			if ("\n"+name+" " in str_):
				str_ = Replace(str_, "\n"+name+" ", "\n"+result+" ")#左换行右空格
			if (" "+name+"#" in str_):
				str_ = Replace(str_, " "+name+"#", " "+result+"#")#右换行左空格
			if (" "+name+"\n" in str_):
				str_ = Replace(str_, " "+name+"\n", " "+result+"\n")#右换行左空格
			if ("#"+name.upper()+" " in str_):
				str_ = Replace(str_, "#"+name.upper()+" ", "#"+result+" ")#左换行右空格且全大写
			if ("\n"+name.upper()+" " in str_):
				str_ = Replace(str_, "\n"+name.upper()+" ", "\n"+result+" ")#左换行右空格且全大写
			if (" "+name.upper()+"#" in str_):
				str_ = Replace(str_, " "+name.upper()+"#", " "+result+"#")#右换行左空格且全大写
			if (" "+name.upper()+"\n" in str_):
				str_ = Replace(str_, " "+name.upper()+"\n", " "+result+"\n")#右换行左空格且全大写
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
			if ("。"+name in str_):
				str_ = Replace(str_, "。"+name, "。"+result)#左侧有句号
			if ("。"+name.upper() in str_):
				str_ = Replace(str_, "。"+name.upper(), "。"+result)#左侧有句号且全大写
			if ("!"+name in str_):
				str_ = Replace(str_,"!"+name, "!"+result)#左侧有叹号
			if ("!"+name.upper() in str_):
				str_ = Replace(str_, "!"+name.upper(), "!"+result)#左侧有叹号且全大写
			if ("！"+name in str_):
				str_ = Replace(str_, "！"+name, "！"+result)#左侧有全角叹号
			if ("！"+name.upper() in str_):
				str_ = Replace(str_, "！"+name.upper(), "！"+result)#左侧有全角叹号且全大写
			if ("?"+name in str_):
				str_ = Replace(str_, "?"+name, "?"+result)#左侧有问号
			if ("?"+name.upper() in str_):
				str_ = Replace(str_, "?"+name.upper(), "?"+result)#左侧有问号且全大写
			if ("？"+name in str_):
				str_ = Replace(str_, "？"+name, "？"+result)#左侧有全角问号
			if ("？"+name.upper() in str_):
				str_ = Replace(str_, "？"+name.upper(), "？"+result)#左侧有全角问号且全大写
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
			if ("\""+name+"\"" in str_):
				str_ = Replace(str_, "\""+name+"\"", "\""+result+"\"")#左右双引号
			if ("'"+name+"'" in str_):
				str_ = Replace(str_, "'"+name+"'", "'"+result+"'")#左右单引号
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

result = []

file = open(input("Strings.json: ").replace("\\","/"), 'r', encoding='utf-8')
content = json.loads(file.read())["Strings"]
file.close()

print("正在下载：人名文本")
req = requests.get(r"")
Names = json.loads(req.text)
req = requests.get(r"")
Names_en = json.loads(req.text)

for line in content:
	result.append(ReplaceName(line, Names, Names_en))
file = open("strings_name.json", 'w', encoding='utf-8')
file.write(json.dumps({"Strings": result}, indent=4, ensure_ascii=False))
file.close()