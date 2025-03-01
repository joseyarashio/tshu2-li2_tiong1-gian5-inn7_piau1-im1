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
from 臺灣言語工具.基本元素.公用變數 import 標點符號
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 處理中研院標音.音標錯誤表 import 音標錯誤表
from 臺灣言語工具.音標系統.閩南語.通用拼音音標 import 通用拼音音標

class 第三步整理文本格式:
	粗胚 = 文章粗胚()
	def 整理(self, 分堆句):
		資料 = []
		for 分堆 in 分堆句:
			資料.append(self.整理一句(分堆))
		return 資料
	def 整理一句(self, 分堆):
		(標籤, 漢羅, 音標) = 分堆
		新音標 = 音標.strip('-').replace(',', ' ').strip()
# 		新音標 = 新音標.replace('- ', '-')
		新音標 = 新音標.replace('_', '-')
		新音標 = self.粗胚.數字英文中央全加分字符號(新音標)
		for 錯, 著 in 音標錯誤表:
			新音標 = 新音標.replace(錯, 著)
		新音標 = self.粗胚.建立物件語句前處理減號(通用拼音音標, 新音標)
		新漢羅 = 漢羅
		for 符號 in 標點符號:
			新漢羅 = 新漢羅.replace(符號, ' ')
		新漢羅 = 新漢羅.replace('ｅ', ' e ')
		新漢羅 = self.粗胚.數字英文中央全加分字符號(新漢羅)
		新漢羅 = self.粗胚.建立物件語句前處理減號(通用拼音音標, 新漢羅)
		return (標籤.strip(), 新漢羅, 新音標)
