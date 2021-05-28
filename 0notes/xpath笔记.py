Xpath 表达式
    --/：1）表示一个层级。2）表示从根节点开始定位遍理。
	--//：1）表示多个层级。可以表示从任意位置开始定位。
	--属性定位：//div[@class='song']；tag[@attrName='attrValue']
	--索引定位：//div[@class='song']/p[3]，索引是从1开始的。
	--取文本：
	    --/text() 获取标签中直系的文本内容
        --//text() 标签中直系和非直系的文本内容（所有文本内容）
	--取属性：    --/@attrName       ===> img/@src
	--采用or, and, not: tree.xpath('xpath路径1 | xpath路径2')

**********实例代码1:***************
import requests
from lxml import etree

html = requests.get('www.xxxx.com.cn')
tree = etree.HTML(html)
tree.xpath('//xpath路径/text()')[0] #反馈对象位list，所以加[0]取得数据
tree.xpath('//xpath路径1/text() | //xpath路径2/text()')[0]
