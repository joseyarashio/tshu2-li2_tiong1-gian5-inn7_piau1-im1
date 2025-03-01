"""
著作權所有 (C) 民國102年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
import unicodedata
import re

class 第二步拆標題漢羅佮音標:
	頭 = 'dv0219014 中華民國走來台灣後獨立於中華人民共和國之外，/diong2-hua5-vin2-gok2zau1lai3-dai2-uan5-au2,'
	尾 = 'dok3-lip3[li3]-i2-diong2-hua5-rin2-vin5-giong3-hor2-gok2-zi2-qua2'
	分字佮音 = re.compile('(.*?) ([^ ]+[a-zA-Z]*\d.*)')
	毋是音標字元 = re.compile('[^0-9a-zA-Z,_ \-()\[\]]')
	def 拆開(self, 語句):
		資料 = []
		for 句 in 語句:
			if 句 == self.頭:
				句 += self.尾
			elif 句 == self.尾:
				continue
			資料.append(self.拆開一句(句))
		return 資料
	def 拆開一句(self, 句):
		try:
# 			print('句',句)
			標籤, 文本 = 句.split(' ', 1)
			if '/' in 文本:
				切文本 = 文本.rsplit('/', 1)
			if '//' in 文本:
				切文本 = 文本.rsplit('//', 1)
			elif ' ' in 文本:
				切文本 =self.分字佮音.split(文本)[1:3]
# 				print('文本',文本)
# 				print('切文本',切文本)
# 				print('有符號',self.毋是音標字元.findall(切文本[1]))
				if len(self.毋是音標字元.findall(切文本[1]))>0:
					切文本[0]=切文本[0]+' '
				while len(self.毋是音標字元.findall(切文本[1]))>0:
					切文本[0]=切文本[0]+切文本[1][0]
					切文本[1]=切文本[1][1:]
			else:
				切文本=[]
		except:
			print(句)
			raise
		if len(切文本) == 2:
			漢羅, 音標 = 切文本
		else:
			# 揣出文本上尾一个毋是小寫英文、數字佮「,」「-」的所在
			切點 = 0
			for 所在 in range(len(文本)):
				if 文本[所在] == ',' or 文本[所在] == '-' or 文本[所在] == ' ' or \
					文本[所在].isdigit() or unicodedata.category(文本[所在]) == 'Ll':
					pass
				else:
					切點 = 所在
			漢羅 = 文本[:切點 + 1].strip()
			音標 = 文本[切點 + 1:].strip()
		return (標籤, 漢羅, 音標)
