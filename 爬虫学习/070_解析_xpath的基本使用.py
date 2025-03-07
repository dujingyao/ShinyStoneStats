from lxml import etree

# xpath解析
#  （1）本地文件                                            etree.parse
#  （2）服务器响应的数据 response.read().decode('utf-8')     etree.HTML()

# 解析本地文件
tree = etree.parse('xpath的基本使用.html')

# tree.xpath('xpath路径')

# （1）路径查询
# 查找ul下面的li
# //:查找所有的子孙节点，不考虑层级关系
# /:找直接子节点
# li_list = tree.xpath('//ul/li')

# 判断列表的长度
# print(li_list)
# print(len(li_list))

# （2）谓词查询
# 例子：查找所有有id属性的li标签
# text()获取标签中的内容
# li_list = tree.xpath('//ul/li[@id]/text()')

# 查找id为l1的便签 注意引号的问题
# li_list = tree.xpath('//ul/li[@id="l1"]/text()')

# (3)属性查询
# 查找到id为l1的li标签的class的属性值
# li = tree.xpath('//ul/li[@id="l1"]/@class')

# (4)模糊查询
# 查询id中包含l的li便签
# li_list = tree.xpath('//ul/li[contains(@id,"l")]/text()')
# 查询id的值以l为开头的li标签
# li_list = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')


# print(li_list)
