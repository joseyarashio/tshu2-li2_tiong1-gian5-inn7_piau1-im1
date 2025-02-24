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
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.解析整理.文章粗胚 import 文章粗胚
from 臺灣言語工具.解析整理.轉物件音家私 import 轉物件音家私
from 臺灣言語工具.解析整理.物件譀鏡 import 物件譀鏡
from 臺灣言語工具.基本元素.公用變數 import 分詞符號
from 臺灣言語工具.基本元素.公用變數 import 分字符號
from 補全漢全羅.揣全漢全羅 import 揣全漢全羅
class 臆全漢全羅:
	粗胚 = 文章粗胚()
	分析器 = 拆文分析器()
	家私 = 轉物件音家私()
	譀鏡 = 物件譀鏡()
	_全漢全羅 = 揣全漢全羅()
	def 建立(self, 語句):
		資料 = []
		for 句 in 語句:
			資料.append(self.建立一句(句))
		return 資料
	def 建立一句(self, 句):
		(標籤, 漢羅, 變調音標) = 句
		音標句物件 = self.分析器.建立句物件(變調音標)
		補的句物件 = self._全漢全羅.揣(音標句物件)
		漢字 = self.譀鏡.看型(補的句物件, 物件分字符號=分字符號, 物件分詞符號=分詞符號)
		本調音標 = self.譀鏡.看音(補的句物件, 物件分字符號=分字符號, 物件分詞符號=分詞符號)
		return (標籤, 漢羅, 變調音標, 漢字, 本調音標)

if __name__ == '__main__':
	全漢全羅 = 臆全漢全羅()
	print(全漢全羅.建立一句(('sin7-bing5',) * 3))
